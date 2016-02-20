# coding: utf-8


class SettingsException(Exception):
    pass

class UnknownSettingException(SettingsException):
    pass

class SettingsParseException(SettingsException):
    pass
