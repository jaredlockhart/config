# This is an example settings/local.py file.
# These settings overrides what's in settings/base.py

from . import base

# To extend any settings from settings/base.py here's an example:
#INSTALLED_APPS = base.INSTALLED_APPS + ['debug_toolbar']

# This is pretty nice for development:
#MIDDLEWARE_CLASSES = list(base.MIDDLEWARE_CLASSES) + [
#    'webpay.base.middleware.LogExceptionsMiddleware',
#]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'webpay',
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

# By default, BrowserID expects your app to use http://127.0.0.1:8000
# Uncomment the following line if you prefer to access your app via localhost
SITE_URL = 'http://webpay.jaredkerim.com'
DOMAIN = 'webpay.jaredkerim.com'

# Playdoh ships with Bcrypt+HMAC by default because it's the most secure.
# To use bcrypt, fill in a secret HMAC key. It cannot be blank. Date is
# when you added the key, it's unused in the code.
HMAC_KEYS = {
    #'2012-06-06': 'some secret',
}

from django_sha2 import get_password_hashers
PASSWORD_HASHERS = get_password_hashers(base.BASE_PASSWORD_HASHERS, HMAC_KEYS)

# Make this unique, and don't share it with anybody.  It cannot be blank.
SECRET_KEY = 'some_secret-key'

# Should robots.txt allow web crawlers?  Set this to True for production
ENGAGE_ROBOTS = True

# Run Celery synchronously for local development.
CELERY_ALWAYS_EAGER = True
# Uncomment these to activate and customize Celery:
# CELERY_ALWAYS_EAGER = False  # required to activate celeryd
# BROKER_HOST = 'localhost'
# BROKER_PORT = 5672
# BROKER_USER = 'playdoh'
# BROKER_PASSWORD = 'playdoh'
# BROKER_VHOST = 'playdoh'
# CELERY_RESULT_BACKEND = 'amqp'

## Log settings

# SYSLOG_TAG = "http_app_playdoh"  # Make this unique to your project.
# LOGGING = dict(loggers=dict(playdoh={'level': logging.DEBUG}))

# Common Event Format logging parameters
#CEF_PRODUCT = 'Playdoh'
#CEF_VENDOR = 'Mozilla'

# Set this to False if you are running a local development install without
# HTTPS to disable HTTPS-only cookies.
SESSION_COOKIE_SECURE = False

# Uncomment this to see descriptive errors on the JWT verification screen.
#VERBOSE_LOGGING = True

# Get some nice test output.
#NOSE_PLUGINS = [
#    'nosenicedots.NiceDots',
#]
#NOSE_ARGS = [
#    '--logging-clear-handlers',
#    '--with-nicedots',
#]

# Solitude settings (needed for live server or really testing the solitude
# API.)

SOLITUDE_URL = 'http://solitude.jaredkerim.com'
MARKETPLACE_URL = 'http://zamboni.jaredkerim.com'

# Set up your local webpay for payments against a B2G device.
DOMAIN = 'webpay.jaredkerim.com'  # JWT aud
KEY = DOMAIN  # JWT iss
SECRET = 'some-secret-key'

# Add the single page app for local dev.
ENABLE_SPA = False

VERBOSE_LOGGING = True
TEST_PIN_UI = True

base.JS_SETTINGS['zamboni_raven_url'] = 'http://none@zamboni.jaredkerim.com/api/v1/fireplace/report_error/18513'

CACHE_PREFIX = 'webpay'

# When not None, this is a dict of mcc and mnc to simulate a specific mobile
# network. This overrides the client side network detection.
# Example: {'mcc': '123', 'mnc': '45'}
# Use this setting carefully!
SIMULATED_NETWORK = None #{'mcc': '334', 'mnc': '020'}
