import unittest
import os
from unittest.mock import patch

from pytuneteller.pytuneteller import main


class MainTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_main(self):
        with patch('sys.argv', ['pytuneteller', 'virgo']):
            main()

        with patch('sys.argv', ['pytuneteller', '--all']):
            main()

        with patch('sys.argv', ['pytuneteller', 'virgo', '--yesterday']):
            main()

        with patch('sys.argv', ['pytuneteller', 'virgo', '--tomorrow']):
            main()
