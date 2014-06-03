from mkt.settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG
DEBUG_PROPAGATE_EXCEPTIONS = DEBUG

#SITE_URL_OVERRIDE = SITE_URL  = 'http://zamboni.jaredkerim.com'
SITE_URL_OVERRIDE = SITE_URL  = 'http://zamboni.jaredkerim.com'
MEDIA_URL = '/media/' 
STATIC_URL = '/'

# These apps are great during development.
INSTALLED_APPS += (
    'debug_toolbar',
    'django_extensions',
    'fixture_magic',
    'django_qunit',
    'kombu.transport.django',
)

# You want one of the caching backends.  Dummy won't do any caching, locmem is
# cleared every time you restart the server, and memcached is what we run in
# production.
#CACHES = {
#    'default': {
#        'BACKEND': 'django.core.cache.backends.memcached.Memcached',
#        'LOCATION': 'localhost:11211',
#    }
#}
CACHES = {
    'default': {
        'BACKEND': 'caching.backends.memcached.MemcachedCache',
        'LOCATION': ['localhost:11211'],
        'TIMEOUT': 500,
    }
}

CACHE_MACHINE_USE_REDIS = True
REDIS_BACKEND = 'redis://'
# Caching is required for CSRF to work, please do not use the dummy cache.

DATABASES = {
    'default': {
        'NAME': 'zamboni',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'root',
        'OPTIONS': {'init_command': 'SET storage_engine=InnoDB'},
        'TEST_CHARSET': 'utf8',
        'TEST_COLLATION': 'utf8_general_ci',
    },
}

# Skip indexing ES to speed things up?
SKIP_SEARCH_INDEX = False

LOG_LEVEL = logging.DEBUG
HAS_SYSLOG = False

# For debug toolbar.
if DEBUG:
    INTERNAL_IPS = ('127.0.0.1',)
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    DEBUG_TOOLBAR_CONFIG = {
        'HIDE_DJANGO_SQL': False,
        'INTERCEPT_REDIRECTS': False,
    }

# If you're not running on SSL you'll want this to be False.
SESSION_COOKIE_SECURE = False
SESSION_COOKIE_DOMAIN = None

# Run tasks immediately, don't try using the queue.
CELERY_ALWAYS_EAGER = True

# Disables custom routing in settings.py so that tasks actually run.
CELERY_ROUTES = {}

# Disable timeout code during development because it uses the signal module
# which can only run in the main thread. Celery uses threads in dev.
VALIDATOR_TIMEOUT = -1

# The user id to use when logging in tasks. You should set this to a user that
# exists in your site.
# TASK_USER_ID = 1

WEBAPPS_RECEIPT_KEY = os.path.join(ROOT, 'mkt/webapps/tests/sample.key')

# If you want to allow self-reviews for add-ons/apps, then enable this.
# In production we do not want to allow this.
ALLOW_SELF_REVIEWS = True

# For Marketplace payments.
APP_PURCHASE_KEY = 'webpay.jaredkerim.com'
APP_PURCHASE_AUD = 'webpay.jaredkerim.com'
APP_PURCHASE_TYP = 'mozilla-local/payments/pay/v1'
APP_PURCHASE_SECRET = 'some-secret-key'

# Assuming you did `npm install` (and not `-g`) like you were supposed to,
# this will be the path to the `stylus` and `lessc` executables.
STYLUS_BIN = path('node_modules/stylus/bin/stylus')
LESS_BIN = path('node_modules/less/bin/lessc')
LESS_LIVE_REFRESH = True


# Locally we typically don't run more than 1 elasticsearch node. So we set
# replicas to zero.
ES_DEFAULT_NUM_REPLICAS = 0


# LESS
LESS_PREPROCESS = True

# SOLITUDE
SOLITUDE_HOSTS = [
    'http://solitude.jaredkerim.com'
]

AWS_ACCESS_KEY_ID = 'AKIAILSKLJNQHPAJHTEA'
AWS_SECRET_ACCESS_KEY = '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'
S3_BUCKET_ID = 's3.jaredkerim.com'

SENTRY_DSN = 'https://0c7330432f3042b787760a6a2c83be7e:35276a2dcd664125b82b73fe3a6a3298@app.getsentry.com/18513'

BROKER_URL = 'django://'

# A list of the payment providers supported by the marketplace. Currently there
# can be only one value, however we expect this to change in the future.
PAYMENT_PROVIDERS = ['bango', 'boku']#, 'boku']

# When True, pre-generate APKs for apps.
PRE_GENERATE_APKS = False

# The origin URL for our Fireplace frontend, from which API requests come.
FIREPLACE_URL = 'http://fireplace.jaredkerim.com'

QUNIT_TEST_DIRECTORY = ''
