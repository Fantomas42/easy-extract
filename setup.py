"""Installing veliberator"""
from setuptools import setup, find_packages
import sys, os

from easy_extract import VERSION

setup(
    name='easy-extract',
    version=VERSION,
    zip_safe=False,

    scripts=['./bin/easy_extract',],
    packages=find_packages(exclude=['tests',]),
    include_package_data=True,     
    test_suite = 'tests.global_test_suite',

    author='Fantomas42',
    author_email='fantomas42@gmail.com',
    url='http://fantomas.willbreak.it',
 
    license='GPL',
    platforms = 'any',
    description='Easy extraction of archives collections',
    long_description=open(os.path.join('README.rst')).read(),
    keywords='extract, rar, zip, xtm',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Utilities',
        ],
    )
