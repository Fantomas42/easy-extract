Easy-extract
============

.. contents::

Easy-extract try to be a simple and universal multipart unarchiver,
it is designed to extract and repair collections of many archives format 
*(rar, zip, xtm)* in one command line.

Very usefull when you grab on Usenet and you have many archives in differents directory.

Installation
------------

Before you start using easy-extract, you must install these softwares :

 * unrar-free
 * 7zip-full
 * par2

Then use easy_install

    $> easy_install easy-extract

Usage
-----

Usage: easy_extract [options] [directory]

Options:
  --version         show program's version number and exit
  -h, --help        show this help message and exit
  -f, --force       Do not prompt confirmation message
  -n, --not-repair  Do not try to repair archives on errors
  -r, --recursive   Find archives recursively

Simply run **easy_extract** in the directory where the collections are. 

    $> easy_extract

or for finding archives recursivly in a directory.

    $> easy_extract -r my_archives/

All the archives found will be prompted, then confirm the extraction.
Go make a coffee, the script will do the rest !
Easy_extract will handle the repair if the archives are corrupted.

The code
--------

If you want to reuse the code to find archives you can do something like that :

  >>> from easy_extract.archive_finder import ArchiveFinder
  >>> from easy_extract.archives.rar import RarArchive
  >>>
  >>> archive_finder = ArchiveFinder('./my_path/', recursive=True, [RarArchive,])
  >>> archive_finder.archives
  ... [<easy_extract.archives.rar.RarArchive object at 0x...>, <easy_extract.archives.rar.RarArchive object at 0x...>]
