# -*- coding: utf-8 -*-
import random
from pytuneteller.sites import Site


class PytunetellerABC:
    pass


class Pytuneteller(PytunetellerABC):
    pass


class PytunetellerCLI(PytunetellerABC):

    @classmethod
    def run(cls, sign, day='today'):
        klass = random.choice(Site.all())
        print(klass.get_horoscope(sign=sign, day=day))
