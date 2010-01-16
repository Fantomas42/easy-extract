"""Unit tests for XtmArchive object"""
import os
import unittest

from easy_extract.archives.xtm import XtmArchive

class XtmArchiveTestCase(unittest.TestCase):

    def test_is_archive_file(self):
        self.assertTrue(XtmArchive.is_archive_file('file.xtm'))
        self.assertTrue(XtmArchive.is_archive_file('file.XTM'))
        self.assertEquals(XtmArchive.is_archive_file('file.XTM'), 'file')
        self.assertFalse(XtmArchive.is_archive_file('file.xt'))

        self.assertEquals(XtmArchive.is_archive_file('file.xtm'), 'file')
        self.assertEquals(XtmArchive.is_archive_file('file.001.xtm'), 'file')
        self.assertEquals(XtmArchive.is_archive_file('file.011.xtm'), 'file')
        self.assertEquals(XtmArchive.is_archive_file('file.111.xtm'), 'file')
        self.assertEquals(XtmArchive.is_archive_file('File.avi.111.xtm'), 'File.avi')
        self.assertFalse(XtmArchive.is_archive_file('file.011.xt'))

    def test__extract(self):
        filenames = ['archive.001.xtm',
                     'archive.002.xtm',
                     'archive.003.xtm',]
        archive = XtmArchive('archive', '.', filenames)
        def toto(cmd):
            print cmd
        
        original = os.system
        os.system = toto
        archive._extract()

        os.system = original

suite = unittest.TestLoader().loadTestsFromTestCase(XtmArchiveTestCase)


