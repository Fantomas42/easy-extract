"""Find and build the archives"""
import os

from easy_extract.archive import Archive
from easy_extract.utils import get_filename_name

class ArchiveFinder(object):
    """Find and build the archives contained in path"""

    def __init__(self, path='.', recursive=True, archive_classes=[]):
        self.root_path = path
        self.recursive = recursive
        self.archive_classes = archive_classes
        
        self.path_archives_found = self.find_archives(self.root_path,
                                                      self.recursive,
                                                      self.archive_classes)

    def is_archive_file(self, filename, archive_classes=[]):
        """Check if the filename is associated to an
        archive class"""
        for archive_class in archive_classes:
            if archive_class.is_archive_file(filename):
                return archive_class
        return False

    def get_path_archives(self, path, filenames=[], archive_classes=[]):
        """Build and return Archives list from a path"""
        archives = {}
            
        for filename in filenames:
            archive_class = self.is_archive_file(filename, archive_classes)
            
            if archive_class:
                name = get_filename_name(filename)
                archives.setdefault(name, archive_class(name, path))
                archives[name].append(filename)

        return archives.values()

    def find_archives(self, path, recursive, archive_classes=[]):
        """Walk to the root_path finding archives"""
        path_archives = {}

        for (dirpath, dirnames, filenames) in os.walk(path):
            path_archives[dirpath] = self.get_path_archives(dirpath, filenames,
                                                            archive_classes)
            if not recursive:
                break
                
        return path_archives

    @property
    def archives(self):
        """Return all Archives found"""
        archives = []
        for ars in self.path_archives_found.values():
            archives.extend(ars)
        return archives
            
    def __len__(self):
        """The length is equals to Archives found"""
        return len(self.archives)

    def __iter__(self):
        """Iterate around the Archives found"""
        for archive in self.archives:
            yield archive

    def __str__(self):
        return 'ArchiveFinder %s %s' % (self.path, self.recursive)
    
