"""Archive collection modules"""
import os

CHAR_TO_ESCAPE = (' ', '(', ')', '*', "'", '"', '&')


class BaseFileCollection(object):
    """Base file collection"""

    def __init__(self, name, path='.', filenames=[]):
        self.name = name
        self.path = path
        self.filenames = filenames

    @property
    def files(self):
        return self.filenames

    def escape_filename(self, filename):
        """Escape a filename"""
        for char in CHAR_TO_ESCAPE:
            filename = filename.replace(char, '\%s' % char)
        return filename

    def get_path_filename(self, filename):
        """Concatenate path and filename"""
        return os.path.join(self.path, filename)

    def get_command_filename(self, filename):
        """Convert filename for command line"""
        return self.escape_filename(self.get_path_filename(filename))

    def remove(self):
        """Remove all files collection"""
        return os.system('rm -f %s' % ' '.join(
            [self.get_command_filename(f) for f in self.files]))


class MedKit(BaseFileCollection):
    """MedKit is collection of par2 files"""

    def __init__(self, name, path='.', filenames=[]):
        super(MedKit, self).__init__(name, path, filenames)
        self.medkits = []
        self.find_medkits(self.filenames)

    @property
    def files(self):
        return self.medkits

    def is_medkit_file(self, filename):
        """Check if the filename is a medkit"""
        return bool(filename.startswith(self.name) and
                    filename.lower().endswith('.par2'))

    def find_medkits(self, filenames=[]):
        """Find files for building the medkit"""
        for filename in filenames:
            if self.is_medkit_file(filename) and filename not in self.medkits:
                self.medkits.append(filename)
        self.medkits.sort()

    def check_and_repair(self, silent=False):
        """Check and repair with medkits"""
        if self.medkits:
            options = silent and '-qq' or ''
            root_medkit = self.get_command_filename(self.medkits[0])
            extra_kits = '%s*' % self.get_command_filename(self.name)
            command = 'par2 r %s %s %s' % (options, root_medkit, extra_kits)
            result = os.system(command)
            return bool(not result)
        return False


class Archive(MedKit):
    """Archive is a collection of archive files and a MedKit"""
    archive_type = 'undefined'
    ALLOWED_EXTENSIONS = []

    def __init__(self, name, path='.', filenames=[]):
        super(Archive, self).__init__(name, path, filenames)
        self.archives = []
        self.find_archives(self.filenames)

    @property
    def files(self):
        return self.archives + self.medkits

    @classmethod
    def is_archive_file(cls, filename):
        """Check if the filename is allowed for the Archive"""
        for regext in cls.ALLOWED_EXTENSIONS:
            if regext.search(filename):
                return regext.split(filename)[0]
        return False

    def find_archives(self, filenames=[]):
        """Find files for building the archive"""
        for filename in filenames:
            if (filename.startswith(self.name) and
                self.is_archive_file(filename) and
                    filename not in self.archives):
                self.archives.append(filename)
        self.archives.sort()

    def extract(self, repair=True):
        """Extract the archive and do integrity checking"""
        extraction = self._extract()

        if not extraction and repair:
            if self.check_and_repair():
                extraction = self._extract()

        return extraction

    def _extract(self):
        """Extract the archive"""
        raise NotImplementedError

    def __str__(self):
        if self.medkits:
            return '%s (%i %s archives, %i par2 files)' % (
                self.name, len(self.archives),
                self.archive_type, len(self.medkits))
        return '%s (%i %s archives)' % (
            self.name, len(self.archives), self.archive_type)
