"""HJ Split archive format"""
import os
import re

from easy_extract.archive import Archive

EXTENSIONS = [re.compile('.\d{3}$', re.I),]

class HJSplitArchive(Archive):
    """The HJ Split format"""
    ALLOWED_EXTENSIONS = EXTENSIONS

    def _extract(self):        
        new_filename = self.escape_filename(self.name)
        first_archive = self.get_command_filename(self.archives[0])

        print 'Extracting %s...' % new_filename
        
        os.system('cat %s > %s' % (first_archive, new_filename))

        for archive in self.archives[1:]:
            archive = self.get_command_filename(archive)
            os.system('cat %s >> %s' % (archive, new_filename))

        return True

