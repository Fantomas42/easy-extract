"""Renamed archive format"""
import re

from easy_extract.archive import Archive

EXTENSIONS = [re.compile('\.\d+$', re.I)]


class RenamedArchive(Archive):
    """
    Renamed archive format,
    the archive type is undefined and behave like a fallback.
    """
    ALLOWED_EXTENSIONS = EXTENSIONS

    def _extract(self):
        return True
