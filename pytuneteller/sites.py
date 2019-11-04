"""
Contains class for multiple websites
"""
import requests
from bs4 import BeautifulSoup


"""
TODO: Add clean method
"""


class BaseSite:

    url = None
    sites = []

    @classmethod
    def parse(cls, **kwargs):
        raise NotImplementedError('parse not implemented yet.')

    @classmethod
    def _request(cls, url):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36'
        }
        return requests.get(url, verify=False, headers=headers)

    @classmethod
    def apply_custom_actions(cls, func, text):
        if not func:
            return text
        return func(text)

    @classmethod
    def get_horoscope(cls, sign, day='today'):
        return f'Source [{cls.__name__}]: {cls.parse(sign=sign, day=day)}'
        # return cls.apply_custom_actions(lambda text: text.upper(), cls.parse(sign=sign))


class Astrology(BaseSite):

    url = 'https://astrology.com/horoscope/daily/{day}/{sign}.html'

    @classmethod
    def parse(cls, **kwargs):
        sign = kwargs.get('sign')
        day = kwargs.get('day', 'today')

        response = cls._request(cls.url.format(day=day, sign=sign))
        soup = BeautifulSoup(response.text, 'html.parser')
        parent = soup.select_one('span.date').parent
        parent.select_one('span.date').decompose()  # Delete date from parent
        horoscope = parent.text

        return horoscope


class GaneshaSpeaks(BaseSite):

    url = 'https://www.ganeshaspeaks.com/horoscopes/{day}-horoscope/{sign}/'

    @classmethod
    def parse(cls, **kwargs):
        sign = kwargs.get('sign')
        day = kwargs.get('day', 'daily')
        day = 'daily' if day == 'today' else day

        response = cls._request(cls.url.format(day=day, sign=sign))
        soup = BeautifulSoup(response.text, 'html.parser')
        horoscope = soup.find('div', {'id': 'daily'}).find(
            'div', {'class': 'row margin-bottom-0'}).find('p').text

        return horoscope


class Horoscope(BaseSite):

    url = 'https://www.horoscope.com/us/horoscopes/general/horoscope-general-daily-{day}.aspx?sign={sign}'

    @classmethod
    def parse(cls, **kwargs):
        sign_mappings = {
            'aries': 1,
            'taurus': 2,
            'gemini': 3,
            'cancer': 4,
            'leo': 5,
            'virgo': 6,
            'libra': 7,
            'scorpio': 8,
            'sagittarius': 9,
            'capricorn': 10,
            'aquarius': 11,
            'pisces': 12
        }
        sign = sign_mappings.get(kwargs.get('sign'))
        day = kwargs.get('day', 'today')

        response = cls._request(cls.url.format(day=day, sign=sign))
        soup = BeautifulSoup(response.text, 'html.parser')
        horoscope = soup.select_one('.switcher + p')
        horoscope.find('strong').decompose()
        horoscope = horoscope.text[3:]
        return horoscope


class Astrosage(BaseSite):

    url = 'http://www.astrosage.com/horoscope/{day}-{sign}-horoscope.asp'

    @classmethod
    def parse(cls, **kwargs):
        sign = kwargs.get('sign')
        day = kwargs.get('day', 'daily')
        day = 'daily' if day == 'today' else day

        if day == 'yesterday':
            return "Could not get yesterday's horoscope"

        if day == 'tomorrow':
            sign = day
            day = kwargs.get('sign')

        response = cls._request(cls.url.format(day=day, sign=sign))
        soup = BeautifulSoup(response.text, 'html.parser')
        horoscope = soup.select_one(
            '.ui-large-hdg + .ui-large-content.text-justify').text

        return horoscope


class CafeAstrology(BaseSite):

    url = 'https://cafeastrology.com/{sign}dailyhoroscope{day}.html'
    day_mappings = {
        'today': '',
        'yesterday': 'y',
        'tomorrow': 'tom'
    }

    @classmethod
    def parse(cls, **kwargs):
        sign = kwargs.get('sign')
        day = kwargs.get('day', '')

        day = cls.day_mappings[day]

        response = cls._request(cls.url.format(day=day, sign=sign))
        soup = BeautifulSoup(response.text, 'html.parser')
        _img = soup.select_one('.wp-image-10891')
        print(response.url)
        horoscope = _img.parent.parent
        # _img.decompose()
        return horoscope.text


class AstrologyZodiacSign(BaseSite):
    url = 'https://www.astrology-zodiac-signs.com/horoscope/{sign}/{day}/'

    @classmethod
    def parse(cls, **kwargs):
        sign = kwargs.get('sign')
        day = kwargs.get('day', 'daily')
        day = 'daily' if day == 'today' else day

        response = cls._request(cls.url.format(day=day, sign=sign))
        soup = BeautifulSoup(response.text, 'html.parser')

        class_selector = '.yesterdaysHoroscope' if day == 'yesterday' else '.dailyHoroscope'
        target = soup.select_one(class_selector)
        horoscope = []
        print(response.url)
        for el in target.select('p'):
            horoscope.append(el.text)

        return '\n'.join(horoscope)


class Site:

    sites = []

    @classmethod
    def register(cls, klass):
        cls.sites.append(klass)

    @classmethod
    def all(cls):
        return cls.sites


Site.register(Astrology)
Site.register(GaneshaSpeaks)
Site.register(Horoscope)
Site.register(Astrosage)
Site.register(CafeAstrology)
Site.register(AstrologyZodiacSign)
