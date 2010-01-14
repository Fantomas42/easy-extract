"""Archive collection modules"""
import os

from easy_extract.utils import escape_filename


class MedKit(object):
    def __init__(self, name, path):
        self.name = name
        self.path = path
        self.medkits = []

    def find_medkits(self, filenames=[]):
        """Find files for building the medkit"""
        if not filenames:
            filenames = os.listdir(self.path)

        for filename in filenames:
            if filename.startswith(self.name) and filename.lower().endswith('.par2'):
                self.medkits.append(filename)

    def check_and_repair(self):
        """Check and repair with medkits"""
        if self.medkits:
            return os.system('par2 r %s' % self.escape_filename(self.medkits[0]))
        return False

class Archive(MedKit):
    """Base class Archive"""

    def __init__(self, name, path='.'):
        self.filenames = []
        super(Archive, self).__init__(name, path)

    def extract(self, check=False):
        """Extract the archive and do integrity checking"""
        if check:
            integrity = self.check_and_repair()
            if not integrity:
                print 'Archive corrompu impossible dextraire'
            
        extraction = self._extract()

        if not extraction and not check_integrity:
            self.extract(True)
        return extraction

    def _extract(self):
        """Extract the archive"""
        raise NotImplementedError

    @classmethod
    def is_archive_file(cls, filename):
        """Check if the filename is allowed in this Archive"""
        return False

    def append(self, filename):
        """Append a filename to the archive's filenames"""
        self.filenames.append(filename)

    def escape_filename(self, filename):
        """Escape a filename"""
        return escape_filename(filename)

    def __str__(self):
        return '%s\n%i files, %i medkits' % (self.filenames[0], len(self.filenames),
                                             len(self.medkits))

