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

from docopt import docopt
from .utils import horoscope_signs as signs
from .version import get_version
from .pytuneteller import PytunetellerCLI
import urllib3
# Disable InsecureRequestWarning
urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)


def main():
    args = docopt(__doc__, version=get_version(), options_first=False)
    sign = args.get('<sign>').lower() if args.get('<sign>') else ''
    day = 'today'

    if args.get('--yesterday'):
        day = 'yesterday'

    if args.get('--tomorrow'):
        day = 'tomorrow'

    PytunetellerCLI.run(sign, day)
