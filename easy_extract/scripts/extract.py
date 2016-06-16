import os
import sys
from optparse import OptionParser

from easy_extract import __version__
from easy_extract.scripts.index import EasyIndex
from easy_extract.archives.xtm import XtmArchive
from easy_extract.archives.rar import RarArchive
from easy_extract.archives.renamed import RenamedArchive
from easy_extract.archives.hj_split import HJSplitArchive
from easy_extract.archives.seven_zip import SevenZipArchive
from easy_extract.archive_finder import ArchiveFinder


class EasyExtract(ArchiveFinder):
    """User interface for extracting archives"""

    def __init__(self, paths, recursive=False,
                 force_extract=False, repair=True,
                 repair_only=False, clean=False):
        self.excludes = []
        self.clean = clean
        self.repair = repair
        self.repair_only = repair_only
        self.force_extract = force_extract

        super(EasyExtract, self).__init__(paths, recursive,
                                          [RarArchive, SevenZipArchive,
                                           XtmArchive, HJSplitArchive,
                                           RenamedArchive])

        if self.can_extract(self.force_extract):
            self.extract_archives(self.repair,
                                  self.repair_only,
                                  self.clean)
        else:
            sys.exit('No archives to extract !')

    def get_path_archives(self, path, filenames, archive_classes):
        print 'Scanning %s...' % os.path.abspath(path)
        archives = super(EasyExtract, self).get_path_archives(
            path, filenames, archive_classes)
        return archives

    def can_extract(self, force):
        if self.archives:
            if force or len(self.archives) == 1:
                return True
            for archive in self.archives:
                print archive

            extract = raw_input('%i archives found. Extract all ? '
                                '[Y]es / No / Select : ' % len(self.archives))
            if not extract or 'y' in extract.lower():
                return True
            if 's' in extract.lower():
                for archive in self.archives:
                    extract = raw_input(
                        'Extract %s ? [Y]es / No / All / Quit : ' % archive)
                    extract = extract.lower()
                    if extract:
                        if 'n' in extract:
                            self.excludes.append(archive)
                        elif 'a' in extract:
                            break
                        elif 'q' in extract:
                            index = self.archives.index(archive)
                            self.excludes.extend(self.archives[index:])
                            break

                return bool(len(self.archives) - len(self.excludes))
        return False

    def extract_archives(self, repair, repair_only, clean):
        for archive in self.archives:
            if archive not in self.excludes:
                if repair_only:
                    archive.check_and_repair()
                else:
                    success = archive.extract(repair)
                    if success and clean:
                        archive.remove()


def cmdline():
    parser = OptionParser(usage='Usage: %prog [options] [directory]...',
                          version='%prog ' + __version__)
    parser.add_option('-f', '--force', dest='force_extract',
                      action='store_true', default=False,
                      help='Do not prompt confirmation message')
    parser.add_option('-n', '--not-repair', dest='repair',
                      action='store_false', default=True,
                      help='Do not try to repair archives on errors')
    parser.add_option('-c', '--repair-only', dest='repair_only',
                      action='store_true', default=False,
                      help='Do only a check and repair operation')
    parser.add_option('-r', '--recursive', dest='recursive',
                      action='store_true', default=False,
                      help='Find archives recursively')
    parser.add_option('-k', '--keep', dest='clean',
                      action='store_false', default=True,
                      help='Do not delete archives on success')
    parser.add_option('-x', '--no-index', dest='index',
                      action='store_false', default=True,
                      help='Do not index the extracted files')

    (options, args) = parser.parse_args()

    directories = ['.']
    if len(args):
        directories = args

    print '--** Easy Extract v%s **--' % __version__
    EasyExtract(directories, options.recursive,
                options.force_extract, options.repair,
                options.repair_only, options.clean)
    if options.index and not options.repair_only:
        EasyIndex(directories, options.recursive)
