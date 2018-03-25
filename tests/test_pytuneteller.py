#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `pytuneteller` package."""


import unittest

from pytuneteller import pytuneteller

from pytuneteller.utils import generate_funny_name
from pytuneteller.exceptions import InvalidHoroscope, InvalidType


class TestPytuneteller(unittest.TestCase):
    """Tests for `pytuneteller` package."""

    def setUp(self):
        """Set up test fixtures, if any."""
        self.funny_name = generate_funny_name()
        self.horoscopes = pytuneteller._all_horoscope('today')
        self.horoscope = pytuneteller.get_horoscope(sign='virgo', site='astrology')

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_get_all_horoscopes(self):
        self.assertIs(type(self.horoscopes), dict)

    def test_get_horoscope(self):
        self.assertIs(type(self.horoscope), str)

    def test_print_horoscope(self):
        for sign, horoscope in self.horoscopes.items():
            pytuneteller.print_horoscope(sign, horoscope)
