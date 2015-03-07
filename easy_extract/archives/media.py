"""Media archive file format"""
import os
import re

from easy_extract.archive import Archive

RAW_EXTENSIONS = ['\.AVI', '\.OGG', '\.OGV',
                  '\.MP4', '\.MPG', '\.MPEG',
                  '\.MKV', '\.M4V']

EXTENSIONS = [re.compile('%s$' % ext, re.I) for ext in RAW_EXTENSIONS]


class MediaArchive(Archive):
    """The Rar format Archive"""
    archive_type = 'media'
    ALLOWED_EXTENSIONS = EXTENSIONS

    def _extract(self):
        first_archive = self.get_command_filename(self.archives[0])
        return not os.system('synoindex -a %s' % first_archive)
