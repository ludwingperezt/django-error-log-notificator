from __future__ import unicode_literals

from django.conf import settings

USER_SETTINGS = getattr(settings, "DB_NOTIFICATION", None)

DEFAULTS = {
    'DB_NAME': 'db_notification',
    'LOG_LEVEL_DEBUG': 'DEBUG',
    'LOG_LEVEL_INFO': 'INFO',
    'LOG_LEVEL_WARNING': 'WARNING',
    'LOG_LEVEL_ERROR': 'ERROR',
    'LOG_LEVEL_CRITICAL': 'CRITICAL',
}

class DBNotificationSettings(object):
    def __init__(self, user_settings=None, defaults=None):
        self.user_settings = user_settings or {}
        self.defaults = defaults or {}

    def __getattr__(self, attr):
        if attr not in self.defaults.keys():
            raise AttributeError("Invalid DB_NOTIFICATION setting: %r" % (attr))

        try:
            val = self.user_settings[attr]
        except KeyError:
            val = self.defaults[attr]

        setattr(self, attr, val)

        return val

db_notification_settings = DBNotificationSettings(USER_SETTINGS, DEFAULTS)