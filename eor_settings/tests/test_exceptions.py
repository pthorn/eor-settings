import unittest
from unittest.mock import MagicMock

from eor_settings import *


class TestExceptions(unittest.TestCase):

    def test_unknown_exception(self):
        reset()

        with self.assertRaises(UnknownSettingException):
            get_setting('app.are_you_there')

    def test_not_present_exception(self):
        reset()

        with self.assertRaises(SettingNotPresentException):
            ParseSettings({}).string('are_you_still_there')

    def test_convert_exception(self):
        reset()

        settings = {
            'app.bad_int': 'meow'
        }

        with self.assertRaises(ConvertException):
            ParseSettings(settings).int('bad_int')

    def test_variant_exception(self):
        reset()

        settings = {
            'app.bad_variant': 'meow'
        }

        with self.assertRaises(BadVariantException):
            ParseSettings(settings).string('bad_variant', variants=['v1', 'v2'])


if __name__ == '__main__':
    unittest.main()
