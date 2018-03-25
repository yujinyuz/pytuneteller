# -*- coding: utf-8 -*-

"""pytuneteller

Usage:
    pytuneteller (-h | --help)
    pytuneteller --version
    pytuneteller --all
    pytuneteller [(--yesterday | --today | --tomorrow)]
    pytuneteller [<sign>]
    pytuneteller [<sign> (--yesterday | --today | --tomorrow)]


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
    pytuneteller --yesterday
    pytuneteller virgo --today
    pytuneteller gemini --yesterday
"""


import logging
import random
import requests
import urllib3

from pytuneteller.exceptions import InvalidHoroscope
from pytuneteller.utils import generate_funny_name
from pytuneteller.utils import horoscope_signs as signs
from pytuneteller.version import get_version


from docopt import docopt
from bs4 import BeautifulSoup

# Disable InsecureRequestWarning
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)
logger = logging.getLogger(__name__)


supported_sites = ['astrology', 'ganeshaspeaks']
funny_name = ""


def print_horoscope(sign, text, day='today', emoji='\U0001F608'):
    format = """
{lines}
    A fortune has been casted upon you by a {name} {emoji}
    {sign} {sign_icon} ({date})
        {text}
{lines}
    """
    print(format.format(sign=sign.capitalize(), sign_icon=signs[sign], text=text, date=day.capitalize(), name=funny_name, emoji=emoji, lines='\U0000269A'*79))


def get_horoscope(sign, day='today', site=None):

    def _astrology():
        site = 'https://astrology.com/horoscope/daily/{day}/{sign}.html'.format(sign=sign, day=day)
        h_soup = BeautifulSoup(_fetch_request(site).text, 'lxml')
        horoscope = h_soup.find('div', {'class': 'daily-horoscope'}).find('p').text

        return horoscope

    def _ganeshaspeaks():
        d = 'daily' if day == 'today' else day
        site = 'https://www.ganeshaspeaks.com/horoscopes/{day}-horoscope/{sign}/'.format(sign=sign, day=d)
        h_soup = BeautifulSoup(_fetch_request(site).text, 'lxml')
        horoscope = h_soup.find('div', {'id': 'daily'}).find('div', {'class': 'row margin-bottom-0'}).find('p').text
        # TODO(yujinyuz): replace Ganesha with a funny name before returning the findings.
        horoscope = horoscope.replace('Ganesha', funny_name)

        return horoscope

    def _random_horoscope_findings(horoscope_sites=supported_sites):
        rand_choice = random.choice(horoscope_sites)
        random_site = horoscope_site_mapping[rand_choice]
        return random_site()

    horoscope_site_mapping = {
        'astrology': _astrology,
        'ganeshaspeaks': _ganeshaspeaks,
    }

    if not site:
        horoscope_findings = _random_horoscope_findings()
    else:
        horoscope_findings = horoscope_site_mapping[site]()

    return horoscope_findings


def _all_horoscope(day='today'):
    horoscopes = {}
    print("Fetching all horoscopes \U000023F3")
    for sign, sign_icon in signs.items():
        print("Chanting spells to foresee the future of {sign} {sign_icon}".format(sign=sign.capitalize(), sign_icon=sign_icon))
        horoscope = get_horoscope(sign, day)
        horoscopes[sign] = horoscope

    return horoscopes


def _fetch_request(url):
    return requests.get(url, verify=False)


def main():
    args = docopt(__doc__, version=get_version(), options_first=False)
    sign = args.get('<sign>').lower() if args.get('<sign>') else ""
    global funny_name
    funny_name = generate_funny_name()
    day = 'today'

    if args.get('--yesterday'):
        day = 'yesterday'

    if args.get('--tomorrow'):
        day = 'tomorrow'

    get_all_horoscopes = args.get('--all')

    if sign not in signs.keys() and not get_all_horoscopes:
        raise InvalidHoroscope

    if sign:
        horoscope = get_horoscope(sign, day)
        print_horoscope(sign, horoscope, day)
    else:
        horoscopes = _all_horoscope(day)
        for sign, horoscope in horoscopes.items():
            funny_name = generate_funny_name()
            print_horoscope(sign, horoscope, day)


if __name__ == '__main__':
    main()
