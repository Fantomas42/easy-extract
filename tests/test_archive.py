"""Unit tests for Archive object"""
import unittest

from easy_extract.archive import Archive
from easy_extract.utils import escape_filename

class ArchiveTestCase(unittest.TestCase):

    default_name = 'archive_name'

    def test_init(self):
        a = Archive(self.default_name)
        self.assertEquals(a.name, self.default_name)
        self.assertEquals(a.path, '.')
        
        a = Archive(self.default_name, './tests')
        self.assertEquals(a.name, self.default_name)
        self.assertEquals(a.path, './tests')

    def test_extract(self):
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

        self.assertEquals(len(a.medkit), 0)
        a.find_medkit()
        self.assertEquals(len(a.medkit), 0)
        filenames = ['%s.par2' % self.default_name,
                     '%s.vol00+02.par2' % self.default_name,
                     '%s.vol01+03.PAR2' % self.default_name,
                     '%s.nzb' % self.default_name]
        a.find_medkit(filenames)
        self.assertEquals(len(a.medkit), 3)

suite = unittest.TestLoader().loadTestsFromTestCase(ArchiveTestCase)
