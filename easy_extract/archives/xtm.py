"""Xtm archive format"""
import os
import re

from easy_extract.archive import Archive

EXTENSIONS = [re.compile('.\d{3}.xtm$', re.I),
              re.compile('.xtm$', re.I)]


class XtmArchive(Archive):
    """The XTM archive format"""
    archive_type = 'xtm'
    ALLOWED_EXTENSIONS = EXTENSIONS

    def _extract(self):
        new_filename = self.escape_filename(self.name)
        first_archive = self.get_command_filename(self.archives[0])

        print 'Extracting %s...' % new_filename

        os.system('dd if=%s skip=1 ibs=104 status=noxfer > %s 2>/dev/null' % \
                  (first_archive, new_filename))

        for archive in self.archives[1:]:
            archive = self.get_command_filename(archive)
            os.system('cat %s >> %s' % (archive, new_filename))

        return True
