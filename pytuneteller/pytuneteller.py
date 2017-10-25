# -*- coding: utf-8 -*-

"""pytuneteller

Usage:
    pytuneteller (-h | --help)
    pytuneteller --version
    pytuneteller [horoscopes] [(--yesterday | --today | --tomorrow)]
    pytuneteller [horoscope] [<sign>]
    pytuneteller [horoscope] [<sign> (--yesterday | --today | --tomorrow)]


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
    pytuneteller horoscopes
    pytuneteller horoscopes --yesterday
    pytuneteller horoscope virgo --today
    pytuneteller horoscope pisces --yesterday
"""


import json
import logging
import random
import requests
import urllib3

from .exceptions import InvalidHoroscope
from .utils import generate_funny_name
from .version import get_version

from datetime import datetime

from docopt import docopt
from bs4 import BeautifulSoup

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

supported_sites = ['astrology', 'ganeshaspeaks']

def print_horoscope(sign, text, day='today', name=None):

    name = name if name else generate_funny_name()

    format = """
{lines}
    A fortune has been casted upon you by a {name}!!!
    {sign} ({date})
        {text}
{lines}
    """
    print(format.format(sign=sign.capitalize(), text=text, date=day, name=name, lines="="*79))

def get_horoscope(sign, day='today'):

    def _astrology():
        site = 'https://astrology.com/horoscope/daily/{day}/{sign}.html'.format(sign=sign, day=day)
        h_soup = BeautifulSoup(fetch_request(site).text, 'lxml')
        horoscope = h_soup.find('div', {'class': 'daily-horoscope'}).find('p').text

        return horoscope

    def _ganeshaspeaks():
        d = 'daily' if day == 'today' else day
        site = 'https://www.ganeshaspeaks.com/horoscopes/{day}-horoscope/{sign}/'.format(sign=sign, day=d)
        h_soup = BeautifulSoup(fetch_request(site).text, 'lxml')
        horoscope = h_soup.find('div', {'id': 'daily'}).find('div', {'class': 'row margin-bottom-0'}).find('p').text
        # TODO(yujinyuz): replace Ganesha with a funny name before returning the findings.

        return horoscope

    def _random_horoscope_findings(horoscope_sites=supported_sites):
        rand_choice = random.choice(horoscope_sites)
        random_site = horoscope_site_mapping[rand_choice]
        return random_site()

    horoscope_site_mapping = {
        'astrology': _astrology,
        'ganeshaspeaks': _ganeshaspeaks,
    }

    horoscope_findings = _random_horoscope_findings()

    return horoscope_findings

def all_horoscope(day='today'):
    horoscopes = {}
    print("Fetching all horoscopes...")
    for sign in signs:
        print("Chanting spells to foresee the future of {sign}.".format(sign=sign.capitalize()))
        horoscope = get_horoscope(sign, day)
        horoscopes[sign] = horoscope

    return horoscopes


def fetch_request(url):
    return requests.get(url, verify=False)


def main():
    args = docopt(__doc__, version=get_version(), options_first=False)
    sign = args.get('<sign>').lower() if args.get('<sign>') else ""
    day = 'today'
    single_horoscope = args.get('horoscope')
    all_horoscopes = args.get('horoscopes')

    if args.get('--yesterday'):
        day = 'yesterday'
    if args.get('--tomorrow'):
        day = 'tomorrow'

    if sign not in signs and not all:
        raise InvalidHoroscope

    if single_horoscope:
        horoscope = get_horoscope(sign, day)
        print_horoscope(sign, horoscope, day)

    if all_horoscopes:
        horoscopes = all_horoscope(day)
        for sign, horoscope in horoscopes.items():
            print_horoscope(sign, horoscope, day)


if __name__ == '__main__':
    main()
