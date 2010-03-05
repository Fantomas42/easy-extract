"""Unit tests for HJSplitArchive object"""
import os
import unittest

from easy_extract.archives.hj_split import HJSplitArchive

class HJSplitArchiveTestCase(unittest.TestCase):

    def test_is_archive_file(self):
        self.assertTrue(HJSplitArchive.is_archive_file('file.001'))
        self.assertTrue(HJSplitArchive.is_archive_file('file.011'))
        
        self.assertFalse(HJSplitArchive.is_archive_file('file.01'))

    def test__extract(self):
        system_commands = []
        def fake_system(cmd):
            system_commands.append(cmd)
        original_system = os.system
        os.system = fake_system
        
        filenames = ['archive.001',
                     'archive.002',
                     'archive.003',]
        archive = HJSplitArchive('archive', './path', filenames)
        self.assertTrue(archive._extract())
        self.assertEquals(system_commands,  ['cat ./path/archive.001 > archive',
                                             'cat ./path/archive.002 >> archive',
                                             'cat ./path/archive.003 >> archive'])        
        os.system = original_system

    def test_extract(self):
        name = 'test_hjsplit.txt'
        dirpath = './tests/data/hjsplit'
        archive = HJSplitArchive(name, dirpath,
                                 os.listdir(dirpath))
        self.assertTrue(archive.extract())

        result = open(name, 'r')
        self.assertEquals(result.read(), '123456789')
        result.close()
        os.system('rm -rf %s' % name)
        

suite = unittest.TestLoader().loadTestsFromTestCase(HJSplitArchiveTestCase)
