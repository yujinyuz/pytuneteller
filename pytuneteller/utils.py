import random
import os

from pytuneteller.exceptions import InvalidType

BASE_DIR = os.path.dirname(__file__)

horoscope_signs = {
    'aries': '\U00002648',
    'taurus': '\U00002649',
    'gemini': '\U0000264A',
    'cancer': '\U0000264B',
    'leo': '\U0000264C',
    'virgo': '\U0000264D',
    'libra': '\U0000264E',
    'scorpio': '\U0000264F',
    'sagittarius': '\U00002650',
    'capricorn': '\U00002651',
    'aquarius': '\U00002652',
    'pisces': '\U00002653'
}


def generate_funny_name(adjectives=[], nouns=[]):
    """
    Adjectives and Nouns should accept a list of words.
    Returns a random generated name.
    """

    if not ((type(adjectives) is list) or (type(nouns) is list)):
        raise InvalidType

    adjective_path = os.path.join(BASE_DIR, 'words', 'adjectives.txt')
    nouns_path = os.path.join(BASE_DIR, 'words', 'nouns.txt')

    if not (adjectives and nouns):
        with open(adjective_path) as adjective_f, open(nouns_path) as nouns_f:

            adjectives = [adjective.strip('\n') for adjective in adjective_f]
            nouns = [noun.strip('\n') for noun in nouns_f]

    funny_name = "{adjective} {noun}".format(adjective=random.choice(adjectives), noun=random.choice(nouns))

    return funny_name
