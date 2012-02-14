"""HJ Split archive format"""
import os
import re

from easy_extract.archive import Archive

EXTENSIONS = [re.compile('.\d{3}$', re.I)]


class HJSplitArchive(Archive):
    """The HJ Split format"""
    archive_type = 'hj-split'
    ALLOWED_EXTENSIONS = EXTENSIONS

    def check_and_repair(self, silent=False):
        """Custom check and repair with medkits"""
        if self.medkits:
            options = silent and '-qq' or ''
            root_medkit = self.get_command_filename(self.medkits[0])
            medkit_extensions = self.get_command_filename(
                '%s.0*' % self.name)
            result = os.system('par2 r %s %s %s' % (
                options, root_medkit, medkit_extensions))
            return bool(not result)
        return False

    def _extract(self):
        new_filename = self.escape_filename(self.name)
        first_archive = self.get_command_filename(self.archives[0])

        print 'Extracting %s...' % new_filename

        os.system('cat %s > %s' % (first_archive, new_filename))

        for archive in self.archives[1:]:
            archive = self.get_command_filename(archive)
            os.system('cat %s >> %s' % (archive, new_filename))

        return True
