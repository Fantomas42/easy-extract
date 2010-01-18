"""Unit tests for XtmArchive object"""
import os
import unittest

from easy_extract.archives.xtm import XtmArchive

class XtmArchiveTestCase(unittest.TestCase):

    def test_is_archive_file(self):
        self.assertTrue(XtmArchive.is_archive_file('file.xtm'))
        self.assertTrue(XtmArchive.is_archive_file('file.XTM'))
        self.assertTrue(XtmArchive.is_archive_file('file.001.xtm'))
        self.assertTrue(XtmArchive.is_archive_file('file.011.xtm'))
        self.assertTrue(XtmArchive.is_archive_file('file.111.xtm'))
        self.assertTrue(XtmArchive.is_archive_file('File.avi.111.xtm'))

        self.assertFalse(XtmArchive.is_archive_file('file.xt'))
        self.assertFalse(XtmArchive.is_archive_file('file.011.xt'))
        self.assertFalse(XtmArchive.is_archive_file('file.rar'))
        self.assertFalse(XtmArchive.is_archive_file('file.xtm.ext'))

    def test__extract(self):
        system_commands = []
        def fake_system(cmd):
            system_commands.append(cmd)
        original_system = os.system
        os.system = fake_system
        
        filenames = ['archive.001.xtm',
                     'archive.002.xtm',
                     'archive.003.xtm',]
        archive = XtmArchive('archive', './path', filenames)
        archive._extract()
        self.assertEquals(system_commands, [
            'dd if=./path/archive.001.xtm skip=1 ibs=104 status=noxfer > ./path/archive 2>/dev/null',
            'cat ./path/archive.002.xtm >> ./path/archive',
            'cat ./path/archive.003.xtm >> ./path/archive'])
        
        os.system = original_system

suite = unittest.TestLoader().loadTestsFromTestCase(XtmArchiveTestCase)


