"""Rar archive format"""
import os

from easy_extract.archive import Archive

EXTENSIONS = []
for i in range(100):
    if i < 10:
        EXTENSIONS.append('.r0%i' % i)
        EXTENSIONS.append('.part0%i.rar' % i)
    else:
        EXTENSIONS.append('.r%i' % i)
        EXTENSIONS.append('.part%i.rar' % i)
EXTENSIONS.append('.rar')


class RarArchive(Archive):
    """The Rar format Archive"""
    ALLOWED_EXTENSIONS = EXTENSIONS
    
    def _extract(self):
        first_archive = self.get_command_filename(self.archives[0])
        return not os.system('unrar e %s' % first_archive)

