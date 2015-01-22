"""
Django settings for tstat project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '(agu(vr_ls5(!y*h^m@=*ih#oucm9^)jewwz!^g0+x@auj%hz4'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'dash',
    'debug_toolbar',
    'djangobower',
    'crispy_forms'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tstat.urls'

WSGI_APPLICATION = 'tstat.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tstat'
    }
}

####################################################
#######             CRISPY FORMS             #######
####################################################

CRISPY_TEMPLATE_PACK = 'bootstrap3'

####################################################
#######                BOWER                 #######
####################################################

BOWER_INSTALLED_APPS = (
    'bootstrap',
    'jquery',
    'jquery-ui'
)

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'dash/static')

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

DATE_INPUT_FORMATS = (
    '%d-%M-%Y', '%d/%m/%Y', '%m/%d/%y', # '25-10-2006', '25/10/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
)

LANGUAGE_CODE = 'en-gb'

TIME_ZONE = 'UTC'


USE_I18N = True

USE_L10N = False

DATE_FORMAT = 'j N Y'

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
)
TEMPLATE_DIRS = (os.path.join(BASE_DIR, 'templates/html'),)
