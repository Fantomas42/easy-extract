"""Global suite of tests"""
import unittest

from tests.test_utils import suite as utils_suite
from tests.test_archive import suite as archive_suite
from tests.test_archive_finder import suite as archive_finder_suite
from tests.test_archive_xtm import suite as archive_xtm_suite
from tests.test_archive_default import suite as archive_default_suite

global_test_suite = unittest.TestSuite([
    utils_suite,
    archive_suite,
    archive_finder_suite,
    archive_default_suite,
    archive_xtm_suite,
    ])
