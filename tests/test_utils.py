"""Unit tests for utils functions"""
import unittest

from easy_extract.utils import get_filename_name
from easy_extract.utils import escape_filename

class UtilsTestCase(unittest.TestCase):

    def test_get_filename_name(self):
        self.assertEquals(get_filename_name('toto'), 'toto')
        self.assertEquals(get_filename_name('toto.titi'), 'toto')
        self.assertEquals(get_filename_name('toto.titi.tata'), 'toto')

    def test_escape_filename(self):
        self.assertEquals(escape_filename('"Coding is *Beautiful* & (Sexy)"'),
                          '\\"Coding\\ is\\ \\*Beautiful\\*\\ \\&\\ \\(Sexy\\)\\"')

suite = unittest.TestLoader().loadTestsFromTestCase(UtilsTestCase)
