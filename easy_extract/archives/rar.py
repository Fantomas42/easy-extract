"""Rar archive format"""
import os
import re

from easy_extract.archive import Archive

EXTENSIONS = [re.compile('.r\d{2}$', re.I),
              re.compile('.part\d+.rar$', re.I),
              re.compile('.rar$', re.I)]

class RarArchive(Archive):
    """The Rar format Archive"""
    ALLOWED_EXTENSIONS = EXTENSIONS
    
    def _extract(self):
        if '%s.rar' % self.name in self.archives:
            first_archive = self.get_command_filename('%s.rar' % self.name)
        else:
            first_archive = self.get_command_filename(self.archives[0])
        
        return not os.system('unrar e %s' % first_archive)

