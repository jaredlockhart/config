# This is an example settings/local.py file.
# These settings overrides what's in settings/base.py

# To extend any settings from settings/base.py here's an example:
from . import base
INSTALLED_APPS = base.INSTALLED_APPS + ('django_extensions',)
#INSTALLED_APPS = base.INSTALLED_APPS + ('debug_toolbar')

# If this is deployed in Stackato, the database config will be
# supplied automatically. Otherwise, we provide db info here:
if not base.DATABASES:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'solitude',
            'USER': 'root',
            'PASSWORD': 'root',
            'HOST': '',
            'PORT': '',
            'OPTIONS': {
                'init_command': 'SET storage_engine=InnoDB',
                'charset': 'utf8',
                'use_unicode': True,
            },
            'TEST_CHARSET': 'utf8',
            'TEST_COLLATION': 'utf8_general_ci',
        },
        # 'slave': {
        #     ...
        # },
    }

# Uncomment this and set to all slave DBs in use on the site.
# SLAVE_DATABASES = ['slave']

# Recipients of traceback emails and other notifications.
ADMINS = (
    # ('Your Name', 'your_email@domain.com'),
)
MANAGERS = ADMINS

# Debugging displays nice error messages, but leaks memory. Set this to False
# on all server instances and True only for development.
DEBUG = TEMPLATE_DEBUG = True

# Is this a development instance? Set this to True on development/master
# instances and False on stage/prod.
DEV = True

# Set up bcrypt.
HMAC_KEYS = {
    '2011-01-01': 'cheesecake',
}
from django_sha2 import get_password_hashers
PASSWORD_HASHERS = get_password_hashers(base.BASE_PASSWORD_HASHERS, HMAC_KEYS)

# Make this unique, and don't share it with anybody.  It cannot be blank.
SECRET_KEY = 'some_secret_key'

## Log settings

# SYSLOG_TAG = "http_app_playdoh"  # Make this unique to your project.
# LOGGING = dict(loggers=dict(playdoh={'level': logging.DEBUG}))

# Common Event Format logging parameters
#CEF_PRODUCT = 'Playdoh'
#CEF_VENDOR = 'Mozilla'

# The Bango API environment. This value must be an existing subdirectory
# under lib/bango/wsdl.
#BANGO_ENV = 'prod'

# Used by OAuth, it cannot be blank.
CLEANSED_SETTINGS_ACCESS = True

SITE_URL = 'http://solitude.jaredkerim.com/'
STATSD_CLIENT = 'django_statsd.clients.null'

# Zippy testing.
#ZIPPY_MOCK = True
ZIPPY_CONFIGURATION = {
    'reference': {
        'url': 'http://zippy.jaredkerim.com',  # No trailing slash.
        'auth': {
            'key': 'dpf43f3p2l4k3l03',
            'secret': 'kd94hf93k423kf44',
            'realm': 'Zippy'
        },
    },
}

# Turning on debug logging for suds looks something like this:

#LOGGING['loggers']['suds.transport'] = {
#    'handlers': ['console'],
#    'level': 'DEBUG',
#}
#LOGGING['loggers']['suds.xsd.schema'] = {
#    'handlers': ['console'],
#    'level': 'DEBUG',
#}
#LOGGING['loggers']['suds.wsdl'] = {
#    'handlers': ['console'],
#    'level': 'DEBUG',
#}

console =  {
    'handlers': ['console'],
    'level': 'DEBUG',
}

LOGGING = {
    'version': 1,
    'handlers': {
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'django.request.tastypie': console,
        'django_browserid': console,
        'statsd': console,
        #'suds': console,
    },
}


AES_KEYS = {
    'buyerpaypal:key': 'buyerpaypal_key.key',
    'buyeremail:key': 'buyeremail_key.key',
    'sellerpaypal:id': 'sellerpaypal_id.key',
    'sellerpaypal:token': 'sellerpaypal_token.key',
    'sellerpaypal:secret': 'sellerpaypal_secret.key',
    'sellerproduct:secret': 'sellerproduct_secret.key',
    'bango:signature': 'bango_signature.key',
}

PAYPAL_MOCK = True

BANGO_AUTH = {
    'USER': 'Mozilla',
    'PASSWORD': 'Qzf6yZUEIUHzTL', 
}

BANGO_NOTIFICATION_URL = SITE_URL + 'notification' 

BOKU_SECRET_KEY = 'zlGCFG3uGIMbZIy9f5garR3PZfLsX1hlKg4rC4ukFNuvNdcDlVWBeqZeIBVyVWRtJDyWsmOkFC5jkwWAwc2ndKNB19D3BokbETs7'
BOKU_MERCHANT_ID = 'mozilla-devs'

NOSE_ARGS = [
    #'--with-progressive',
    '--with-blockage',
    '--nologcapture',
]
