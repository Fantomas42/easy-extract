"""Archive collection modules"""
import os

from easy_extract.utils import escape_filename

_archive_classes_registered = []

def register_archive_class(archive_class):
    _archive_classes_registered.append(archive_class)

def unregister_archive_class(archive_class):
    _archive_classes_registered.remove(archive_class)

def get_archive_classes():
    return _archive_classes_registered

class Archive(object):
    """Base class Archive"""

    def __init__(self, name, path='.'):
        self.name = name
        self.path = path
        self.filenames = []
        self.medkit = []

    def extract(self, *ka, **kw):
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

    def find_medkit(self, filenames=[]):
        """Find files for building the medkit"""
        if not filenames:
            filenames = os.listdir(self.path)

        for filename in filenames:
            if filename.startswith(self.name) and filename.lower().endswith('.par2'):
                self.medkit.append(filename)

