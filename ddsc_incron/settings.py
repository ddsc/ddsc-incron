# Note that logging to a single file from multiple processes is NOT supported.
# See: http://docs.python.org/2/howto/logging-cookbook.html
# #logging-to-a-single-file-from-multiple-processes
# This very much applies to ddsc-incron!

# TODO: Consider ConcurrentLogHandler on pypi when this bug is solved?
# https://bugzilla.redhat.com/show_bug.cgi?id=858912

LOGGING = {
    'version': 1,
    'formatters': {
        'verbose': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'verbose',
            'level': 'DEBUG',
        },
        'null': {
            'class': 'logging.NullHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['null'],
            'level': 'DEBUG',
        },
    }
}

try:
    # Allow each environment to override these settings.
    from ddsc_incron.localsettings import *  # NOQA
except ImportError:
    pass
