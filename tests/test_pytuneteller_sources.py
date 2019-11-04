from vcr_unittest import VCRTestCase

from pytuneteller.sites import Astrology, AstrologyZodiacSign, Astrosage, CafeAstrology, GaneshaSpeaks, Horoscope

import unittest

import pytest


class SourcesTestCase(VCRTestCase):

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.sign = 'virgo'

    @pytest.mark.vcr()
    def test_astrology(self):
        horoscope = Astrology.get_horoscope(self.sign)
        self.assertIn(
            "A sweet group conversation could move", horoscope)

    @pytest.mark.vcr()
    def test_astrology_zodiac_sign(self):
        horoscope = AstrologyZodiacSign.get_horoscope(self.sign)
        self.assertIn("You are free to do as you please", horoscope)

    @pytest.mark.vcr()
    def test_astrosage(self):
        horoscope = Astrosage.get_horoscope(self.sign)
        self.assertIn(
            "Your anger could create a mountain out of molehill-which would only upset your family members.", horoscope)

    @pytest.mark.vcr()
    def test_cafe_astrology(self):
        horoscope = CafeAstrology.get_horoscope(self.sign)
        self.assertIn(
            "Mars transiting your solar second house these days is great", horoscope)

    @pytest.mark.vcr()
    def test_ganesha_speaks(self):
        horoscope = GaneshaSpeaks.get_horoscope(self.sign)
        self.assertIn(
            "Today you will find yourself overflowing with ideas.", horoscope)

    @pytest.mark.vcr()
    def test_horoscope(self):
        horoscope = Horoscope.get_horoscope(self.sign)
        self.assertIn(
            "Today you may be powerfully attracted to someone from a distant state or foreign country.", horoscope)
