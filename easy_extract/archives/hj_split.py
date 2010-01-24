"""HJ SpLIT archive format"""
import os
import re

from easy_extract.archive import Archive

EXTENSIONS = [re.compile('.\d{3}$', re.I),]

class HJSplitArchive(Archive):
    """The HJ Split format"""
    ALLOWED_EXTENSIONS = EXTENSIONS

    def _extract(self):
        new_filename = self.escape_filename(self.name)
        # new_filename = self.get_command_filename(self.name)
        archives = '%s*' % os.path.join(self.path, self.name)

        os.system('cat %s > %s' % (archives, new_filename))
        return True

