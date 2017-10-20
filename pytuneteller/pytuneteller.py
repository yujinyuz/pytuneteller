# -*- coding: utf-8 -*-

"""pytuneteller

Usage:
    pytuneteller (-h | --help)
    pytuneteller horoscope <sign>
    pytuneteller horoscope <sign> (--yesterday | --today | --tomorrow)
    pytuneteller horoscope --all (--yesterday | --today | --tomorrow)

Options:
    -h --help               Show this screen.
    --version               Show version.
    --all                   Displays all horoscopes for today.
    --today                 Get horoscope for today.
                            [default: True]
    --yesterday             Get horoscope for yesterday.
                            [default: False]
    --tomorrow              Get horoscope for tomorrow.
                            [default: False]

Examples:
    pytuneteller horoscope virgo --today
    pytuneteller horoscope pisces --yesterday
"""

import json
import logging
import requests
import urllib3
from docopt import docopt
from bs4 import BeautifulSoup

# Disable InsecureRequestWarning
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger(__name__)

# Horoscope mapping
ARIES = 1
TAURUS = 2
GEMINI = 3
CANCER = 4
LEO = 5
VIRGO = 6
LIBRA = 7
SCORPIO = 8
SAGITTARIUS = 9
CAPRICORN = 10
AQUARIUS = 11
PISCES = 12

signs = {
    ARIES: 'aries',
    TAURUS: 'taurus',
    GEMINI: 'gemini',
    CANCER: 'cancer',
    LEO: 'leo',
    VIRGO: 'virgo',
    LIBRA: 'libra',
    SCORPIO: 'scorpio',
    SAGITTARIUS: 'sagittarius',
    CAPRICORN: 'capricorn',
    AQUARIUS: 'aquarius',
    PISCES: 'pisces',
}

# Horoscope sites [Get a random site (?)]
horoscope_sites = [
    # requires sign as str. ['virgo', 'pisces',]
    'https://astrology.com/horoscope/daily/{day}/{sign}.html',

    # requires sign as int [1, 2, 3]
    'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={sign}',
]

def print_horoscope(horoscope, text):
    format = """
    {horoscope}
        {text}
    """

    print(format.format(horoscope=horoscope.capitalize(), text=text))

def get_horoscope(sign):
    pass

def fetch_request(url):
    return requests.get(url, verify=False)

def main():
    args = docopt(__doc__)

    sign = args.get('<sign>')
    day = 'today'
    if args.get('--yesterday'):
        day = 'yesterday'
    if args.get('--tomorrow'):
        day = 'tomorrow'

    horoscope_soup = BeautifulSoup(fetch_request(horoscope_sites[0].format(day=day, sign=sign)).text, 'lxml')
    horoscope = horoscope_soup.find('div', {'class': 'daily-horoscope'}).find('p').text
    print_horoscope(sign, horoscope)

if __name__ == '__main__':
    main()
