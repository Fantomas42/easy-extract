"""Unit tests for XtmArchive object"""
import os
import unittest

from easy_extract.archives.xtm import XtmArchive

class XtmArchiveTestCase(unittest.TestCase):

    def test_is_archive_file(self):
        self.assertTrue(XtmArchive.is_archive_file('file.xtm'))
        self.assertTrue(XtmArchive.is_archive_file('file.XTM'))
        self.assertFalse(XtmArchive.is_archive_file('file.xt'))

    def test__extract(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(XtmArchiveTestCase)


