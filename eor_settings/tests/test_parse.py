import unittest
from unittest.mock import MagicMock

from eor_settings import *


class TestParse(unittest.TestCase):

    def test_basic_values(self):
        reset()

        settings = {
            'app.str': 'meow',
            'app.int': '34'
        }

        ParseSettings(settings).string('str').int('int')

        self.assertEquals(get_setting('app.str'), 'meow')
        self.assertEquals(get_setting('app.int'), 34)

    def test_bools(self):
        reset()

        settings = {
            'app.true1': 'true',
            'app.true2': '1',
            'app.true3': 'yes'
        }

        ParseSettings(settings).bool('true1').bool('true2').bool('true3')

        self.assertIs(get_setting('app.true1'), True)
        self.assertIs(get_setting('app.true2'), True)
        self.assertIs(get_setting('app.true3'), True)


if __name__ == '__main__':
    unittest.main()
