"""7zip archive format"""
import os

from easy_extract.archive import Archive

EXTENSIONS = ['.ARJ', '.CAB', '.CHM', '.CPIO',
              '.DMG', '.HFS', '.LZH', '.LZMA',
              '.NSIS', '.UDF', '.WIM', '.XAR',
              '.Z', '.ZIP', '.GZIP', '.TAR',]

class SevenZipArchive(Archive):
    """The DefaultArchive use 7z"""
    ALLOWED_EXTENSIONS = EXTENSIONS
    
    def _extract(self):
        first_archive = self.escape_filename(self.archives[0])
        os.system('7z e %s' % first_archive)
    
