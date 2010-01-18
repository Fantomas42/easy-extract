"""Rar archive format"""
import os
import re

from easy_extract.archive import Archive

EXTENSIONS = [re.compile('.r\d{2}$', re.I),
              re.compile('.part\d{2}.rar$', re.I),
              re.compile('.rar$', re.I)]

class RarArchive(Archive):
    """The Rar format Archive"""
    ALLOWED_EXTENSIONS = EXTENSIONS
    
    def _extract(self):
        first_archive = self.get_command_filename(self.archives[0])
        return not os.system('unrar e %s' % first_archive)

