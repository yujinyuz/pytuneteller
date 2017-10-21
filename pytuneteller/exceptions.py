class InvalidHoroscope(Exception):

    def __init__(self):
        Exception.__init__(self, "Seems like you aren't using the right horoscope sign.")
