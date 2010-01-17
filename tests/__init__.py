"""Global suite of tests"""
import unittest

from tests.test_archive import suite as archive_suite
from tests.test_archive_finder import suite as archive_finder_suite
from tests.test_archive_xtm import suite as archive_xtm_suite
from tests.test_archive_rar import suite as archive_rar_suite
from tests.test_archive_seven_zip import suite as archive_seven_zip_suite

global_test_suite = unittest.TestSuite([
    archive_suite,
    archive_finder_suite,
    archive_rar_suite,
    archive_seven_zip_suite,
    archive_xtm_suite,
    ])
