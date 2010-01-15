"""Unit tests for DefaultArchive object"""
import os
import unittest

from easy_extract.archives.default import DefaultArchive

class DefaultArchiveTestCase(unittest.TestCase):

    def test_is_archive_file(self):
        self.assertTrue(DefaultArchive.is_archive_file('file.ARJ'))
        self.assertTrue(DefaultArchive.is_archive_file('file.arj'))
        self.assertTrue(DefaultArchive.is_archive_file('file.cab'))
        self.assertTrue(DefaultArchive.is_archive_file('file.chm'))
        self.assertTrue(DefaultArchive.is_archive_file('file.cpio'))
        self.assertTrue(DefaultArchive.is_archive_file('file.dmg'))
        self.assertTrue(DefaultArchive.is_archive_file('file.hfs'))
        self.assertTrue(DefaultArchive.is_archive_file('file.lzh'))
        self.assertTrue(DefaultArchive.is_archive_file('file.lzma'))
        self.assertTrue(DefaultArchive.is_archive_file('file.nsis'))
        self.assertTrue(DefaultArchive.is_archive_file('file.rar'))
        self.assertTrue(DefaultArchive.is_archive_file('file.udf'))
        self.assertTrue(DefaultArchive.is_archive_file('file.wim'))
        self.assertTrue(DefaultArchive.is_archive_file('file.xar'))
        self.assertTrue(DefaultArchive.is_archive_file('file.z'))

    def test__extract(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(DefaultArchiveTestCase)

