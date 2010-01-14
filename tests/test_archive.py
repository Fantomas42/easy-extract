"""Unit tests for Archive object"""
import os
import unittest

from easy_extract.archive import MedKit
from easy_extract.archive import Archive
from easy_extract.archive import BaseFileCollection
from easy_extract.utils import escape_filename

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
        string_to_escape = 'File Archive "3".ext'

        self.assertEquals(bfc.escape_filename(string_to_escape),
                          escape_filename(string_to_escape))

    def test_get_path_filename(self):
        bfc = BaseFileCollection(self.default_name, '.', ['file1.ext', 'file2.ext'])
        self.assertEquals(bfc.filenames[0], 'file1.ext')
        self.assertEquals(bfc.get_path_filename(bfc.filenames[0]), './file1.ext')
        bfc.path = './tests'
        self.assertEquals(bfc.get_path_filename(bfc.filenames[0]), './tests/file1.ext')

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
        
        a = Archive(self.default_name, './tests')
        self.assertEquals(a.name, self.default_name)
        self.assertEquals(a.path, './tests')

    def test_extract(self):
        pass

    def test__extract(self):
        a = Archive(self.default_name)
        self.assertRaises(NotImplementedError, a.extract)

    def test_is_archive_file(self):
        self.assertFalse(Archive.is_archive_file('file'))

    #def test_append(self):
    #    a = Archive(self.default_name)
    #    
    #    self.assertEquals(len(a.filenames), 0)
    #    a.append('filename')
    #    self.assertEquals(len(a.filenames), 1)

    def test_escape_filename(self):
        a = Archive(self.default_name)
        string_to_escape = 'File Archive "3".ext'
        
        self.assertEquals(a.escape_filename(string_to_escape),
                          escape_filename(string_to_escape))

    def test_find_medkit(self):
        a = Archive(self.default_name, './tests/data')

        self.assertEquals(len(a.medkits), 0)
        a.find_medkits()
        self.assertEquals(len(a.medkits), 0)
        filenames = ['%s.par2' % self.default_name,
                     '%s.vol00+02.par2' % self.default_name,
                     '%s.vol01+03.PAR2' % self.default_name,
                     '%s.vol01+03.PAR2' % self.default_name,
                     '%s.nzb' % self.default_name]
        a.find_medkits(filenames)
        self.assertEquals(len(a.medkits), 3)

    def test_check_and_repair(self):
        pass

suite = unittest.TestSuite([
    unittest.TestLoader().loadTestsFromTestCase(BaseFileCollectionTestCase),
    unittest.TestLoader().loadTestsFromTestCase(MedKitTestCase),
    unittest.TestLoader().loadTestsFromTestCase(ArchiveTestCase)])
