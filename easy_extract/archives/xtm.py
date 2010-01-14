"""Xtm archive format"""
from easy_extract.archive import Archive

class XtmArchive(Archive):
    """The XTM archive format"""

    @classmethod
    def is_archive_file(cls, filename):
        filename = filename.lower()
        if filename.endswith('.xtm'):
            return True
        return False

    def _extract(self):
        new_filename = self.escape_filename('%s.avi' % self.name)
        first_archive = self.escape_filename(self.archives[0])
        
        os.system('dd if=%s skip=1 ibs=104 status=noxfer > %s 2>/dev/null' % \
                  (first_filename, new_filename))
        
        for archive in self.archives[1:]:
            archive = self.escape_filename(archive)
            os.system('cat %s >> %s' % (archive, new_filename))
        
