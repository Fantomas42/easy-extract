"""Unit tests for Archive object"""
import unittest

from easy_extract.archive import MedKit
from easy_extract.archive import Archive
from easy_extract.utils import escape_filename


class MedKitTestCase(unittest.TestCase):

    default_name = 'archive_name'

    def test_init(self):
        mk = MedKit(self.default_name, '.')
        self.assertEquals(mk.path, '.')
        self.assertEquals(mk.medkits, [])

    def test_find_medkits(self):
        mk = MedKit(self.default_name, './tests/data')

        self.assertEquals(len(mk.medkits), 0)
        mk.find_medkits()
        self.assertEquals(len(mk.medkits), 0)
        filenames = ['%s.par2' % self.default_name,
                     '%s.vol00+02.par2' % self.default_name,
                     '%s.vol01+03.PAR2' % self.default_name,
                     '%s.nzb' % self.default_name]
        default_name = 'file'

        mk.find_medkits(filenames)
        self.assertEquals(len(mk.medkits), 3)

    def test_check_and_repair(self):
        pass

class ArchiveTestCase(unittest.TestCase):

    default_name = 'archive_name'

    def test_init(self):
        a = Archive(self.default_name)
        self.assertEquals(a.name, self.default_name)
        self.assertEquals(a.path, '.')
        self.assertEquals(a.medkits, [])
        
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

    def test_append(self):
        a = Archive(self.default_name)
        
        self.assertEquals(len(a.filenames), 0)
        a.append('filename')
        self.assertEquals(len(a.filenames), 1)

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
                     '%s.nzb' % self.default_name]
        a.find_medkits(filenames)
        self.assertEquals(len(a.medkits), 3)

    def test_check_and_repair(self):
        pass

suite = unittest.TestSuite([
    unittest.TestLoader().loadTestsFromTestCase(MedKitTestCase),
    unittest.TestLoader().loadTestsFromTestCase(ArchiveTestCase)])
