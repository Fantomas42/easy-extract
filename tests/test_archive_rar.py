"""Unit tests for DefaultArchive object"""
import os
import unittest

from easy_extract.archives.rar import RarArchive
from easy_extract.archive_finder import ArchiveFinder


class RarArchiveTestCase(unittest.TestCase):

    def test_is_archive_file(self):
        self.assertTrue(RarArchive.is_archive_file('file.rar'))
        self.assertTrue(RarArchive.is_archive_file('file.r01'))
        self.assertTrue(RarArchive.is_archive_file('file.R99'))
        self.assertTrue(RarArchive.is_archive_file('file.part42.rar'))

        self.assertFalse(RarArchive.is_archive_file('file'))
        self.assertFalse(RarArchive.is_archive_file('file.r'))
        self.assertFalse(RarArchive.is_archive_file('file.r100'))
        self.assertFalse(RarArchive.is_archive_file('file.rar.ext'))

    def test__extract(self):
        pass

    def test_realcase_1(self):
        filenames = ['fil.usenet4all.S81103.avi.part01.rar',
                     'fil.usenet4all.S81103.avi.part01.rar.par2',
                     'fil.usenet4all.S81103.avi.part01.rar.vol000+01.par2',
                     'fil.usenet4all.S81103.avi.part01.rar.vol001+02.par2',
                     'fil.usenet4all.S81103.avi.part01.rar.vol003+04.par2',
                     'fil.usenet4all.S81103.avi.part01.rar.vol007+08.par2',
                     'fil.usenet4all.S81103.avi.part02.rar',
                     'fil.usenet4all.S81103.avi.part03.rar',
                     'fil.usenet4all.S81103.avi.part04.rar',
                     'fil.usenet4all.S81103.avi.part05.rar',
                     'fil.usenet4all.S81103.avi.part06.rar',]

        af = ArchiveFinder()
        result = af.get_path_archives('path', filenames)
        self.assertEquals(result, [])
        result = af.get_path_archives('path', filenames, [RarArchive,])
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0].name, 'fil.usenet4all.S81103.avi')
        self.assertEquals(len(result[0].archives), 6)
        self.assertEquals(len(result[0].medkits), 5)

    def test_realcase_2(self):
        filenames = ['bs-mbfs.rar',
                     'bs-mbfs.r00',
                     'bs-mbfs.r01',
                     'bs-mbfs.r02',
                     'bs-mbfs.r03',
                     'bs-mbfs.r04',
                     'bs-mbfs.abtt.par2',
                     'bs-mbfs.abtt.vol000+01.par2',
                     'bs-mbfs.abtt.vol001+02.par2',
                     'bs-mbfs.nfo',]

        af = ArchiveFinder()
        result = af.get_path_archives('path', filenames)
        self.assertEquals(result, [])
        result = af.get_path_archives('path', filenames, [RarArchive,])
        self.assertEquals(len(result), 1)
        self.assertEquals(result[0].name, 'bs-mbfs')        
        self.assertEquals(len(result[0].archives), 6)
        self.assertEquals(len(result[0].medkits), 3)

    def test_realcase_3(self):
        filenames = ['tes-lvsf-sample.par2',
                     'tes-lvsf-sample.vol00+1.par2',
                     'tes-lvsf-sample.vol01+2.par2',
                     'tes-lvsf.cd1.par2',
                     'tes-lvsf.cd1.rar',
                     'tes-lvsf.cd1.r00',
                     'tes-lvsf.cd1.r01',
                     'tes-lvsf.cd1.r02',
                     'tes-lvsf.cd1.r03',
                     'tes-lvsf.cd1.vol00+1.par2',
                     'tes-lvsf.cd1.vol01+2.par2',
                     'tes-lvsf.cd2.par2',
                     'tes-lvsf.cd2.r00',
                     'tes-lvsf.cd2.r01']

        af = ArchiveFinder()
        result = af.get_path_archives('path', filenames)
        self.assertEquals(result, [])
        result = af.get_path_archives('path', filenames, [RarArchive,])
        self.assertEquals(len(result), 2)

        for archive in result:
            self.assertTrue(archive.name.startswith('tes-lvsf'))
            if archive.name == 'tes-lvsf.cd1':
                self.assertEquals(len(archive.archives), 5)
                self.assertEquals(len(archive.medkits), 3)
            else:
                self.assertEquals(len(archive.archives), 2)
                self.assertEquals(len(archive.medkits), 1)


suite = unittest.TestLoader().loadTestsFromTestCase(RarArchiveTestCase)

