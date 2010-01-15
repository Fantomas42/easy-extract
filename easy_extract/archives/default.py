"""Default archive format"""
from easy_extract.archive import Archive

ALLOWED_EXTENSIONS = ['ARJ', 'CAB', 'CHM', 'CPIO',
                      'DMG', 'HFS', 'LZH', 'LZMA',
                      'NSIS', 'RAR', 'UDF', 'WIM',
                      'XAR', 'Z']

class DefaultArchive(Archive):
    """The DefaultArchive use 7z"""

    @classmethod
    def is_archive_file(cls, filename):
        filename = filename.lower()
        
        for ext in ALLOWED_EXTENSIONS:
            if filename.endswith('.%s' % ext.lower()):
                return True
        return False

    def _extract(self):
        first_archive = self.escape_filename(self.archives[0])
        os.system('7z %s' % first_archive)
    
