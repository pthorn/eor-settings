# coding: utf-8


class SettingsException(Exception):
    pass

class UnknownSettingException(SettingsException):
    pass

class ConvertException(SettingsException):
    pass

class SettingNotPresentException(SettingsException):
    pass

class BadVariantException(SettingsException):
    pass
