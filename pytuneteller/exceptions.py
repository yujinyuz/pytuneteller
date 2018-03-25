class InvalidHoroscope(Exception):

    def __init__(self):
        Exception.__init__(self, "Seems like you got a weird horoscope sign.")


class InvalidType(Exception):

    def __init__(self):
        Exception.__init__(self, "Are you sure you passed in a list?")
