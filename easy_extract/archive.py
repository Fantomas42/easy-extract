"""Archive collection modules"""
import os

from easy_extract.utils import escape_filename

class BaseFileCollection(object):
    """Base file collection"""
    def __init__(self, name, path='.', filenames=[]):
        self.name = name
        self.path = path
        self.filenames = filenames
        
    def escape_filename(self, filename):
        """Escape a filename"""
        return escape_filename(filename)

    #def get_absolute_path(self, filename):
    #    return os.path.abspath(os.join(self.path, filename))

class MedKit(BaseFileCollection):
    def __init__(self, name, path='.', filenames=[]):
        super(MedKit, self).__init__(name, path, filenames)
        self.medkits = []
        self.find_medkits(self.filenames)

    def is_medkit_file(self, filename):
        """Check if the filename is a medkit"""
        return bool(filename.startswith(self.name) and filename.lower().endswith('.par2'))

    def find_medkits(self, filenames=[]):
        """Find files for building the medkit"""
        if not filenames:
            filenames = os.listdir(self.path)

        for filename in filenames:
            if self.is_medkit_file(filename):
                self.medkits.append(filename)

    def check_and_repair(self):
        """Check and repair with medkits"""
        if self.medkits:
            result = os.system('par2 r %s' % self.escape_filename(self.medkits[0]))
            return bool(not result)
        return False

class Archive(MedKit):
    """Base class Archive"""

    def __init__(self, name, path='.', filenames=[]):
        super(Archive, self).__init__(name, path, filenames)
        self.archives = []
        self.find_archives(self.filenames)

    @classmethod
    def is_archive_file(cls, filename):
        """Check if the filename is allowed in this Archive"""
        return False

    def find_archives(self, filenames=[]):
        """Find files for building the archive"""
        if not filenames:
            filenames = os.listdir(self.path)

        for filename in filenames:
            if self.is_archive_file(filename):
                self.archives.append(filename)

    def extract(self, check=False):
        """Extract the archive and do integrity checking"""
        if check:
            if not self.check_and_repair():
                return False
            
        extraction = self._extract()

        if not extraction and not check:
            extraction = self.extract(True)
        
        return extraction

    def _extract(self):
        """Extract the archive"""
        raise NotImplementedError

    def __str__(self):
        return '%s\n%i files, %i medkits' % (self.archives[0], len(self.archives),
                                             len(self.medkits))

