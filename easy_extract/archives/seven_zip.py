"""7zip archive format"""
import os
import re

from easy_extract.archive import Archive

RAW_EXTENSIONS = ['.ARJ', '.CAB', '.CHM', '.CPIO',
                  '.DMG', '.HFS', '.LZH', '.LZMA',
                  '.NSIS', '.UDF', '.WIM', '.XAR',
                  '.Z', '.ZIP', '.GZIP', '.TAR',]

EXTENSIONS = [re.compile('%s$' % ext, re.I) for ext in RAW_EXTENSIONS]

class SevenZipArchive(Archive):
    """The 7z unarchiver is used for many formats"""
    ALLOWED_EXTENSIONS = EXTENSIONS
    
    def _extract(self):
        first_archive = self.get_command_filename(self.archives[0])
        return not os.system('7z e %s' % first_archive)
    
