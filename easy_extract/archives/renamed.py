"""Renamed archive format"""
import re

from easy_extract.archive import Archive
from easy_extract.archive_finder import ArchiveFinder
from easy_extract.archives.xtm import XtmArchive
from easy_extract.archives.rar import RarArchive
from easy_extract.archives.hj_split import HJSplitArchive
from easy_extract.archives.seven_zip import SevenZipArchive

EXTENSIONS = [re.compile('\.\d+$', re.I)]


class RenamedArchive(Archive):
    """
    Renamed extensions archive format,
    the archive type is undefined and behave like a fallback.
    """
    ALLOWED_EXTENSIONS = EXTENSIONS

    def extract(self, repair=True):
        """
        We will try a repair and relaunch the scan
        for extracting.
        """
        repaired = self.check_and_repair()
        if repaired:
            finder = ArchiveFinder(
                self.path, False,
                [RarArchive, SevenZipArchive,
                 XtmArchive, HJSplitArchive])
            archives = finder.path_archives_found[self.path]
            for archive in archives:
                if archive.name == self.name:
                    archive.extract(False)
