"""Xtm archive format"""
from easy_extract.archive import Archive

XTM_EXTENSIONS = []
for i in range(1000):
    if i < 10:
        XTM_EXTENSIONS.append('.00%i.xtm' % i)
    elif i < 100:
        XTM_EXTENSIONS.append('.0%i.xtm' % i)
    else:
        XTM_EXTENSIONS.append('.%i.xtm' % i)
XTM_EXTENSIONS.append('.xtm')


class XtmArchive(Archive):
    """The XTM archive format"""

    @classmethod
    def is_archive_file(cls, filename):
        filename = filename.lower()

        for ext in XTM_EXTENSIONS:
            if filename.endswith(ext.lower()):
                return filename.split(ext.lower())[0]
        return False

    def _extract(self):
        new_filename = self.get_command_filename(self.name)
        first_archive = self.get_command_filename(self.archives[0])
        
        os.system('dd if=%s skip=1 ibs=104 status=noxfer > %s 2>/dev/null' % \
                  (first_filename, new_filename))
        
        for archive in self.archives[1:]:
            archive = self.get_command_filename(archive)
            os.system('cat %s >> %s' % (archive, new_filename))
        
