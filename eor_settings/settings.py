# coding: utf-8

import logging
log = logging.getLogger(__name__)

from .exceptions import *


app_settings = dict()


class _Marker(object):
    pass

_none = _Marker()


def get_setting(key):
    """
    return an application setting by key
    """
    try:
        return app_settings[key]
    except KeyError:
        raise UnknownSettingException(key)


def reset():
    global app_settings
    app_settings = dict()


class ParseSettings(object):

    def __init__(self, settings, prefix='app'):
        self.settings = settings
        self.prefix = prefix

    def parse(self, name, convert, default=_none, variants=None):
        global app_settings

        key = self.prefix + '.' + name

        if key in self.settings:
            app_settings[key] = convert(self.settings[key])
        else:
            if default is not _none:
                app_settings[key] = default
            else:
                msg = 'required setting %s not present in config' % (key,)
                log.error(msg)
                raise SettingsParseException(msg)

        if variants:
            if app_settings[key] not in variants:
                msg = 'value for setting %s = %s must be one of %s' % (key, app_settings[key], variants)
                log.error(msg)
                raise SettingsParseException(msg)

        return self

    def string(self, *args, **kwargs):
        kwargs['convert'] = str
        return self.parse(*args, **kwargs)

    def path(self, *args, **kwargs):
        # TODO check that path exists
        return self.string(*args, **kwargs)

    def file(self, *args, **kwargs):
        # TODO check that file is readable
        return self.string(*args, **kwargs)

    def bool(self,  *args, **kwargs):
        kwargs['convert'] = as_bool
        return self.parse(*args, **kwargs)

    def int(self,  *args, **kwargs):
        kwargs['convert'] = int
        return self.parse(*args, **kwargs)

    def list(self,  *args, **kwargs):
        kwargs['convert'] = as_list
        return self.parse(*args, **kwargs)


def as_bool(str_val):
    return str_val.lower() in ('true', '1', 'yes')

def as_list(val):
    return val.split()

