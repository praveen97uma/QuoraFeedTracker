"""
Django settings for quora_track project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
MANAGE_PY_DIR = BASE_DIR#os.path.abspath(os.path.join(BASE_DIR, os.path.pardir))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'fw*$!lcu!gruq066&c-9ebsnqwx8e&-h@ww&+5t1&v0kg9w!d#'

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
    'tracker',
    'djcelery',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader'
)

ROOT_URLCONF = 'quora_track.urls'

WSGI_APPLICATION = 'quora_track.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(MANAGE_PY_DIR, "templates"),
)

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "deploy/static")
if not os.path.exists(STATIC_ROOT):
    os.makedirs(STATIC_ROOT)

STATICFILES_DIRS = (
    os.path.join(MANAGE_PY_DIR, "static"),  
)

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tracker.tasks.add',
        'schedule': timedelta(seconds=5),
        'args': (16, 16)
    },
}

CELERY_TIMEZONE = 'UTC'

CELERY_RESULT_BACKEND='djcelery.backends.database:DatabaseBackend'
