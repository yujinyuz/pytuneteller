
"""
    Hard code versions only!
"""

MAJOR_VERSION = "0"
MINOR_VERSION = "1"
MICRO_VERSION = "3"

def get_version():
    return "{major}.{minor}.{micro}".format(major=MAJOR_VERSION, minor=MINOR_VERSION, micro=MICRO_VERSION)
