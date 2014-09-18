import os
import sys
from optparse import OptionParser

from easy_extract import __version__
from easy_extract.archives.media import MediaArchive
from easy_extract.archive_finder import ArchiveFinder


class EasyIndex(ArchiveFinder):
    """User interface for indexing medias"""
    def __init__(self, paths, recursive=False):
        super(EasyIndex, self).__init__(paths, recursive,
                                        [MediaArchive])
        if self.can_index:
            self.index_medias()
        else:
            sys.exit('No medias to index !')

    def get_path_archives(self, path, filenames, archive_classes):
        print 'Scanning %s...' % os.path.abspath(path)
        archives = super(EasyIndex, self).get_path_archives(
            path, filenames, archive_classes)
        return archives

    @property
    def can_extract(self):
        return bool(self.archives)

    def index_medias(self):
        for archive in self.archives:
            print '- Indexing %s' % archive
            archive.extract()


def cmdline():
    parser = OptionParser(usage='Usage: %prog [options] [directory]...',
                          version='%prog ' + __version__)
    parser.add_option('-r', '--recursive', dest='recursive',
                      action='store_true', default=False,
                      help='Find medias recursively')

    (options, args) = parser.parse_args()

    directories = ['.']
    if len(args):
        directories = args

    print '--** Easy Index v%s **--' % __version__
    EasyIndex(directories, options.recursive)
