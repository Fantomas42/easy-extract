"""Xtm archive format"""
import os
from easy_extract.archive import Archive

EXTENSIONS = []
for i in range(1000):
    if i < 10:
        EXTENSIONS.append('.00%i.xtm' % i)
    elif i < 100:
        EXTENSIONS.append('.0%i.xtm' % i)
    else:
        EXTENSIONS.append('.%i.xtm' % i)
EXTENSIONS.append('.xtm')

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

        # Need to return value
