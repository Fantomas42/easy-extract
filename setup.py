"""Installing easy-extract"""
import os
from setuptools import setup
from setuptools import find_packages

import easy_extract

setup(
    name='easy-extract',
    version=easy_extract.__version__,
    zip_safe=False,


    packages=find_packages(exclude=['tests']),
    include_package_data=True,

    author=easy_extract.__author__,
    author_email=easy_extract.__email__,
    url=easy_extract.__url__,

    license=easy_extract.__license__,
    platforms='any',
    description='Easy extraction of archives collections',
    long_description=open(os.path.join('README.rst')).read(),
    keywords='extract, rar, zip, xtm, hjsplit',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: System Administrators',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Utilities',
        ],

    entry_points={
        'console_scripts': [
            'easy-extract=easy_extract.scripts.extract:cmdline'
            'easy-index=easy_extract.scripts.index:cmdline'
        ]
    },
    test_suite='tests.global_test_suite',
)
