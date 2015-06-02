import os
from os.path import expanduser


DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jmbo',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

INSTALLED_APPS = (
    'jmbo_sitemap',
    'foundry',
    'ckeditor',
    'jmbo',
    'photologue',
    'category',
    'likes',
    'secretballot',

    'layers',
    'preferences',
    'publisher',

    'django.contrib.auth',
    'django.contrib.comments',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    'south',
)

ROOT_URLCONF = 'jmbo_sitemap.urls'

USE_TZ = True

SITE_ID = 1

STATIC_URL = '/static/'

CKEDITOR_UPLOAD_PATH = expanduser('~')

SOUTH_TESTS_MIGRATE = False

# Disable celery
CELERY_ALWAYS_EAGER = True
BROKER_BACKEND = 'memory'

TEMPLATE_DIRS = (os.path.realpath(os.path.dirname(__file__)) + '/jmbo_sitemap/tests/templates/',)

# To test layers we need these settings
LAYERS = {'layers': ['basic']}

TEMPLATE_LOADERS = (
    'layers.loaders.filesystem.Loader',
    'django.template.loaders.filesystem.Loader',
    'layers.loaders.app_directories.Loader',
    'django.template.loaders.app_directories.Loader',
)

STATICFILES_FINDERS = (
    'layers.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'layers.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)
