"""Rar archive format"""
import os
import re

from easy_extract.archive import Archive

RAW_EXTENSIONS = []
for i in range(100):
    if i < 10:
        RAW_EXTENSIONS.append('.r0%i' % i)
        RAW_EXTENSIONS.append('.part0%i.rar' % i)
    else:
        RAW_EXTENSIONS.append('.r%i' % i)
        RAW_EXTENSIONS.append('.part%i.rar' % i)
RAW_EXTENSIONS.append('.rar')

EXTENSIONS = [re.compile('%s$' % ext, re.I) for ext in RAW_EXTENSIONS]


class RarArchive(Archive):
    """The Rar format Archive"""
    ALLOWED_EXTENSIONS = EXTENSIONS
    
    def _extract(self):
        first_archive = self.get_command_filename(self.archives[0])
        return not os.system('unrar e %s' % first_archive)

