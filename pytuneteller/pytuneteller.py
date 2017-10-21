# -*- coding: utf-8 -*-

"""pytuneteller

Usage:
    pytuneteller (-h | --help)
    pytuneteller horoscope --all [(--yesterday | --today | --tomorrow)]
    pytuneteller horoscope [<sign>]
    pytuneteller horoscope [<sign> (--yesterday | --today | --tomorrow)]


Options:
    -h --help               Show this screen.
    --version               Show version.
    --all                   Displays all signs with their corresponding horoscope of the day.
    --today                 Get horoscope for today.
                            [default: True]
    --yesterday             Get horoscope for yesterday.
                            [default: False]
    --tomorrow              Get horoscope for tomorrow.
                            [default: False]

Examples:
    pytuneteller horoscope --all
    pytuneteller horoscope virgo --today
    pytuneteller horoscope pisces --yesterday
"""

import json
import logging
import requests
import urllib3
from docopt import docopt
from bs4 import BeautifulSoup
from .exceptions import InvalidHoroscope
# Disable InsecureRequestWarning
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger(__name__)

# Valid horoscope signs
signs = [
    'aries',
    'taurus',
    'gemini',
    'cancer',
    'leo',
    'virgo',
    'libra',
    'scorpio',
    'sagittarius',
    'capricorn',
    'aquarius',
    'pisces'
]

# Horoscope sites [Get a random site (?)]
horoscope_site = 'https://astrology.com/horoscope/daily/{day}/{sign}.html'

def print_horoscope(horoscope, text):
    format = """
    {horoscope}
        {text}
    """

    print(format.format(horoscope=horoscope.capitalize(), text=text))

def get_horoscope(sign, day='today'):
    horoscope_soup = BeautifulSoup(fetch_request(horoscope_site.format(day=day, sign=sign)).text, 'lxml')
    horoscope = horoscope_soup.find('div', {'class': 'daily-horoscope'}).find('p').text

    return horoscope

def fetch_request(url):
    return requests.get(url, verify=False)

def main():
    args = docopt(__doc__)

    sign = args.get('<sign>')

    if sign not in signs:
        raise InvalidHoroscope

    day = 'today'
    if args.get('--yesterday'):
        day = 'yesterday'
    if args.get('--tomorrow'):
        day = 'tomorrow'

    horoscope = get_horoscope(sign, day)
    print_horoscope(sign, horoscope)

if __name__ == '__main__':
    main()
