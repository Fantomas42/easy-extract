"""Unit tests for Archive object"""
import os
import re
import unittest

from easy_extract.archive import MedKit
from easy_extract.archive import Archive
from easy_extract.archive import BaseFileCollection

class BaseFileCollectionTestCase(unittest.TestCase):

    default_name = 'archive_name'

    def test_init(self):
        bfc = BaseFileCollection(self.default_name)
        self.assertEquals(bfc.path, '.')
        self.assertEquals(bfc.name, self.default_name)
        self.assertEquals(bfc.filenames, [])

        bfc = BaseFileCollection(self.default_name, './tests/data', ['filename'])
        self.assertEquals(bfc.path, './tests/data')
        self.assertEquals(bfc.name, self.default_name)
        self.assertEquals(bfc.filenames, ['filename',])

    def test_escape_filename(self):
        bfc = BaseFileCollection(self.default_name, '.')
        self.assertEquals(bfc.escape_filename('"Coding is *Beautiful* & (Sexy)"'),
                          '\\"Coding\\ is\\ \\*Beautiful\\*\\ \\&\\ \\(Sexy\\)\\"')

    def test_get_path_filename(self):
        bfc = BaseFileCollection(self.default_name, '.', ['file1.ext', 'file2.ext'])
        self.assertEquals(bfc.filenames[0], 'file1.ext')
        self.assertEquals(bfc.get_path_filename(bfc.filenames[0]), './file1.ext')
        bfc.path = './tests'
        self.assertEquals(bfc.get_path_filename(bfc.filenames[0]), './tests/file1.ext')

    def test_get_command_filename(self):
        bfc = BaseFileCollection(self.default_name, './my path/*to file*')
        self.assertEquals(bfc.get_command_filename('file 1.txt'),
                          './my\\ path/\\*to\\ file\\*/file\\ 1.txt')

class MedKitTestCase(unittest.TestCase):

    default_name = 'archive_name'

    def test_init(self):
        mk = MedKit(self.default_name)
        self.assertEquals(mk.path, '.')
        self.assertEquals(mk.name, self.default_name)
        self.assertEquals(mk.filenames, [])
        self.assertEquals(mk.medkits, [])

        filenames = ['%s.par2' % self.default_name,
                     '%s.vol00+02.par2' % self.default_name,
                     '%s.vol01+03.PAR2' % self.default_name,
                     '%s.nzb' % self.default_name]
        mk = MedKit(self.default_name, './tests', filenames)
        self.assertEquals(mk.path, './tests')
        self.assertEquals(mk.name, self.default_name)
        self.assertEquals(len(mk.filenames), 4)
        self.assertEquals(len(mk.medkits), 3)

    def test_is_medkit_file(self):
        mk = MedKit(self.default_name)
        self.assertFalse(mk.is_medkit_file('toto'))
        self.assertFalse(mk.is_medkit_file('toto.par2'))
        self.assertTrue(mk.is_medkit_file('%s.par2' % self.default_name))
        self.assertTrue(mk.is_medkit_file('%s.PAR2' % self.default_name))

    def test_find_medkits(self):
        mk = MedKit(self.default_name, './tests/data')

        self.assertEquals(len(mk.medkits), 0)
        mk.find_medkits()
        self.assertEquals(len(mk.medkits), 0)
        filenames = ['%s.vol00+02.par2' % self.default_name,
                     '%s.vol01+03.PAR2' % self.default_name,
                     '%s.vol01+03.PAR2' % self.default_name,
                     '%s.par2' % self.default_name,
                     '%s.nzb' % self.default_name]
        mk.find_medkits(filenames)
        self.assertEquals(len(mk.medkits), 3)
        self.assertEquals(mk.medkits[0], '%s.par2' % self.default_name)

    def test_check_and_repair(self):
        mk = MedKit(self.default_name)
        self.assertEquals(len(mk.medkits), 0)
        self.assertFalse(mk.check_and_repair())

        medkits = ['file.par2', 'file.vol00.par2']
        self.assertFalse(mk.check_and_repair())

        dirpath = './tests/data/medkits'
        mk = MedKit('test_PAR2', dirpath, os.listdir(dirpath))
        self.assertTrue(mk.check_and_repair(silent=True))

class ArchiveTestCase(unittest.TestCase):

    default_name = 'archive_name'

    def test_init(self):
        a = Archive(self.default_name)
        self.assertEquals(a.path, '.')
        self.assertEquals(a.name, self.default_name)
        self.assertEquals(a.filenames, [])
        self.assertEquals(a.medkits, [])
        self.assertEquals(a.archives, [])

        filenames = ['%s.par2' % self.default_name,
                     '%s.ext' % self.default_name,
                     '%s.vol00+02.par2' % self.default_name,
                     '%s.vol01+03.PAR2' % self.default_name,
                     '%s.nzb' % self.default_name]
        a = Archive(self.default_name, './tests', filenames)
        self.assertEquals(a.path, './tests')
        self.assertEquals(a.name, self.default_name)
        self.assertEquals(len(a.filenames), 5)
        self.assertEquals(len(a.medkits), 3)
        self.assertEquals(len(a.archives), 0)

    def test_files(self):
        a = Archive(self.default_name)
        a.medkits = ['toto', 'titi']
        a.archives = ['tata', 'tutu']
        self.assertEquals(len(a.files), 4)

    def test_is_archive_file(self):
        self.assertFalse(Archive.is_archive_file('file'))

        Archive.ALLOWED_EXTENSIONS = [re.compile('.ext$', re.I),]
        self.assertFalse(Archive.is_archive_file('file'))
        self.assertFalse(Archive.is_archive_file('file.ext1'))
        self.assertEquals(Archive.is_archive_file('file.ext'), 'file')
        self.assertEquals(Archive.is_archive_file('file.eXt'), 'file')
        self.assertEquals(Archive.is_archive_file('File.Ext'), 'File')

    def test_find_archives(self):
        filenames = ['%s.rar' % self.default_name,
                     '%s.zip' % self.default_name,
                     'bla.rar']
        a = Archive(self.default_name, './tests')
        self.assertEquals(a.archives, [])
        a.find_archives(filenames)
        self.assertEquals(a.archives, [])
        original_is_archive_file = a.is_archive_file

        def always_archive_file(filename):
            return True

        a.is_archive_file = always_archive_file
        a.find_archives(filenames)
        self.assertEquals(len(a.archives), 2)

        a.is_archive_file = original_is_archive_file

    def test_extract(self):
        original_extract = Archive._extract
        
        def always_extract(cls):
            return True

        Archive._extract = always_extract
        a = Archive(self.default_name)
        self.assertTrue(a.extract())

        def never_extract(cls):
            return False

        Archive._extract = never_extract
        a = Archive(self.default_name)
        self.assertFalse(a.extract())
        self.assertFalse(a.extract(True))

        def notextract_extract(cls):
            extract = cls.i % 2
            cls.i += 1
            return bool(extract)

        def always_repair(silent=True):
            return True

        Archive._extract = notextract_extract
        a = Archive(self.default_name)
        a.i = 0
        self.assertFalse(a.extract())
        self.assertTrue(a.extract())
        self.assertFalse(a.extract(True))
        self.assertTrue(a.extract())

        original_check_and_repair = a.check_and_repair
        a.check_and_repair = always_repair
        self.assertTrue(a.extract(True))
        a.check_and_repair = original_check_and_repair
        self.assertFalse(a.extract())

        Archive._extract = original_extract

    def test__extract(self):
        a = Archive(self.default_name)
        self.assertRaises(NotImplementedError, a.extract)

    def test_str(self):
        a = Archive(self.default_name)
        self.assertEquals(str(a), 'archive_name (0 archives, 0 par2 files)')
        a.archives = range(10)
        a.medkits = range(5)
        self.assertEquals(str(a), 'archive_name (10 archives, 5 par2 files)')

suite = unittest.TestSuite([
    unittest.TestLoader().loadTestsFromTestCase(BaseFileCollectionTestCase),
    unittest.TestLoader().loadTestsFromTestCase(MedKitTestCase),
    unittest.TestLoader().loadTestsFromTestCase(ArchiveTestCase)])
