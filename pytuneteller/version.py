
"""
    Hard-coded versions only!
"""

MAJOR_VERSION = "0"
MINOR_VERSION = "2"
MICRO_VERSION = "0"


def get_version():
    return "{major}.{minor}.{micro}".format(major=MAJOR_VERSION, minor=MINOR_VERSION, micro=MICRO_VERSION)
