"""Unit tests for DefaultArchive object"""
import os
import unittest

from easy_extract.archives.seven_zip import SevenZipArchive
from easy_extract.archive_finder import ArchiveFinder


class SevenZipArchiveTestCase(unittest.TestCase):

    def test_is_archive_file(self):
        self.assertTrue(SevenZipArchive.is_archive_file('file.ARJ'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.arj'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.cab'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.chm'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.cpio'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.dmg'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.gzip'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.hfs'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.lzh'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.lzma'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.nsis'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.tar'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.udf'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.wim'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.xar'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.z'))
        self.assertTrue(SevenZipArchive.is_archive_file('file.zip'))

        self.assertFalse(SevenZipArchive.is_archive_file('file'))
        self.assertFalse(SevenZipArchive.is_archive_file('file.zip.ext'))
        self.assertFalse(SevenZipArchive.is_archive_file('file.r'))
        self.assertFalse(SevenZipArchive.is_archive_file('file.r100'))

    def test__extract(self):
        pass


suite = unittest.TestLoader().loadTestsFromTestCase(SevenZipArchiveTestCase)

