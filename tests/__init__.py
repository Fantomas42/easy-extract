"""Global suite of tests"""
import unittest

from tests.test_utils import suite as utils_suite
from tests.test_archive import suite as archive_suite
from tests.test_archive_finder import suite as archive_finder_suite

global_test_suite = unittest.TestSuite([
    utils_suite,
    archive_suite,
    archive_finder_suite,
    ])
