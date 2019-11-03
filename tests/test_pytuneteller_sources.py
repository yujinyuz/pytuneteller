from vcr_unittest import VCRTestCase

from pytuneteller.sites import Astrology, AstrologyZodiacSign, Astrosage, CafeAstrology, GaneshaSpeaks, Horoscope

import unittest


class SourcesTestCase(VCRTestCase):

    def setUp(self, *args, **kwargs):
        super().setUp(*args, **kwargs)
        self.sign = 'virgo'

    def test_astrology(self):
        horoscope = Astrology.get_horoscope(self.sign)
        self.assertIn(
            "Feelings are not inappropriate tools for making progress.", horoscope)

    def test_astrology_zodiac_sign(self):
        horoscope = AstrologyZodiacSign.get_horoscope(self.sign)
        self.assertIn("In the 19th century", horoscope)

    def test_astrosage(self):
        horoscope = Astrosage.get_horoscope(self.sign)
        self.assertIn(
            "Don't force and compel people to do things for you", horoscope)

    def test_cafe_astrology(self):
        horoscope = CafeAstrology.get_horoscope(self.sign)
        self.assertIn(
            "The Moon moves into your service sector for a couple of days, dear Virgo", horoscope)

    def test_ganesha_speaks(self):
        horoscope = GaneshaSpeaks.get_horoscope(self.sign)
        self.assertIn(
            "Don't procrastinate matters regarding your health, advises Ganesha", horoscope)

    def test_horoscope(self):
        horoscope = Horoscope.get_horoscope(self.sign)
        self.assertIn(
            "Today close friends, a love partner, or children may appear to be in a quiet, melancholy mood.", horoscope)
