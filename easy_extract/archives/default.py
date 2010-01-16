"""Default archive format"""
import re

from easy_extract.archive import Archive

EXTENSIONS = ['.ARJ', '.CAB', '.CHM', '.CPIO',
              '.DMG', '.HFS', '.LZH', '.LZMA',
              '.NSIS', '.UDF', '.WIM', '.XAR',
              '.Z', '.ZIP', '.GZIP', '.TAR',]

RAR_EXTENSIONS = []
for i in range(100):
    if i < 10:
        RAR_EXTENSIONS.append('.r0%i' % i)
        RAR_EXTENSIONS.append('.part0%i.rar' % i)
    else:
        RAR_EXTENSIONS.append('.r%i' % i)
        RAR_EXTENSIONS.append('.part%i.rar' % i)
RAR_EXTENSIONS.append('.RAR')

EXTENSIONS.extend(RAR_EXTENSIONS)

class DefaultArchive(Archive):
    """The DefaultArchive use 7z"""
    ALLOWED_EXTENSIONS = EXTENSIONS
    
    def _extract(self):
        first_archive = self.escape_filename(self.archives[0])
        os.system('7z %s' % first_archive)
    
