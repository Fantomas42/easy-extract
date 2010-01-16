"""Find and build the archives"""
import os


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
            archive_name = archive_class.is_archive_file(filename)
            if archive_name:
                return archive_name, archive_class
        return False, False

    def get_path_archives(self, path, filenames=[], archive_classes=[]):
        """Build and return Archives list from a path"""
        archives = {}
            
        for filename in filenames:
            name, archive_class = self.is_archive_file(filename, archive_classes)
            
            if archive_class and not name in archives.keys():
                archives[name] = archive_class(name, path, filenames)

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

