import os
import logging

SITE_DOMAIN = 'localhost'

MIDDLEWARE_CLASSES += (
    "satchmo_store.shop.SSLMiddleware.SSLRedirect",
        )
TEMPLATE_CONTEXT_PROCESSORS += (
    'satchmo_store.shop.context_processors.settings',
        )
INSTALLED_APPS += (
    'satchmo_store.shop',
    'django.contrib.comments',
    'django.contrib.sitemaps',
    'registration',
    'keyedcache',
    'livesettings',
    'l10n',
    'sorl.thumbnail',
    'satchmo_store.contact',
    'tax',
    'tax.modules.no',
    'tax.modules.area',
    'tax.modules.percent',
    'shipping',
    'product',
    'product.modules.configurable',
    'payment',
    'payment.modules.giftcertificate',
    'satchmo_utils',
    'app_plugins',
        )
SATCHMO_SETTINGS = {
	'SHOP_BASE' : '/',
	'MULTISHOP' : False,
	#'SHOP_URLS' : patterns('satchmo_store.shop.views',)
}

# satchmo local settings

CACHE_TIMEOUT = 60*5

ACCOUNT_ACTIVATION_DAYS = 7

# modify the cache_prefix if you have multiple concurrent stores.
CACHE_PREFIX = "STORE"

#Configure logging
LOGDIR = os.path.abspath(os.path.dirname(__file__))
LOGFILE = "satchmo.log"
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename=os.path.join(LOGDIR, LOGFILE),
                    filemode='w')

# define a Handler which writes INFO messages or higher to the sys.stderr
fileLog = logging.FileHandler(os.path.join(LOGDIR, LOGFILE), 'w')
fileLog.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('%(asctime)s %(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
fileLog.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(fileLog)
logging.getLogger('keyedcache').setLevel(logging.INFO)
logging.info("Satchmo Started")


