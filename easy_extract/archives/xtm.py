"""Xtm archive format"""
import os
import re

from easy_extract.archive import Archive

RAW_EXTENSIONS = []
for i in range(1000):
    if i < 10:
        RAW_EXTENSIONS.append('.00%i.xtm' % i)
    elif i < 100:
        RAW_EXTENSIONS.append('.0%i.xtm' % i)
    else:
        RAW_EXTENSIONS.append('.%i.xtm' % i)
RAW_EXTENSIONS.append('.xtm')

EXTENSIONS = [re.compile('%s$' % ext, re.I) for ext in RAW_EXTENSIONS]

class XtmArchive(Archive):
    """The XTM archive format"""
    ALLOWED_EXTENSIONS = EXTENSIONS

    def _extract(self):
        new_filename = self.get_command_filename(self.name)
        first_archive = self.get_command_filename(self.archives[0])
        
        os.system('dd if=%s skip=1 ibs=104 status=noxfer > %s 2>/dev/null' % \
                  (first_archive, new_filename))
        
        for archive in self.archives[1:]:
            archive = self.get_command_filename(archive)
            os.system('cat %s >> %s' % (archive, new_filename))

        return True
        # Need to return value
