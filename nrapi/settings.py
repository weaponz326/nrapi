"""
Django settings for nrapi project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from datetime import timedelta
from distutils.command.config import config
from pathlib import Path

import os
import sys
import dj_database_url

from django.core.management.utils import get_random_secret_key

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# SECRET_KEY = 'django-insecure-g^w-9rogg_*5&_vqmf$$3c$k6r2h#k)-^%aoq7*n-1m!0!7$eq'
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = os.getenv("DEBUG", "") != "False"
DEVELOPMENT_MODE = os.getenv("DEVELOPMENT_MODE", "") != "False"

# ALLOWED_HOSTS = []
ALLOWED_HOSTS = [
    'localhost',
    'api.netrink.com'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'corsheaders',
    'django_filters',
    'rest_framework',
    'rest_framework.authtoken',
    'djoser',

    # personal
    'suites.personal.users',
    'suites.personal.modules.portal',
    'suites.personal.modules.settings',
    'suites.personal.modules.calendar',
    'suites.personal.modules.budget',
    'suites.personal.modules.notes',
    'suites.personal.modules.accounts',
    'suites.personal.modules.tasks',
    'suites.personal.payments',
    'suites.personal.support',

    # restaurant
    'suites.restaurant.accounts',
    'suites.restaurant.modules.admin',
    'suites.restaurant.modules.portal',
    'suites.restaurant.modules.settings',
    'suites.restaurant.modules.menu',
    'suites.restaurant.modules.staff',
    'suites.restaurant.modules.payments',
    'suites.restaurant.modules.orders',
    'suites.restaurant.modules.kitchen_stock',
    'suites.restaurant.modules.roster',
    'suites.restaurant.modules.tables',
    'suites.restaurant.modules.deliveries',
    'suites.restaurant.modules.reservations',
    'suites.restaurant.modules.customers',

    # school
    'suites.school.accounts',
    'suites.school.modules.admin',
    'suites.school.modules.portal',
    'suites.school.modules.settings',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'nrapi.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'nrapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

if DEVELOPMENT_MODE is True:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }
elif len(sys.argv) > 0 and sys.argv[1] != 'collectstatic':
    if os.getenv("DATABASE_URL", None) is None:
        raise Exception("DATABASE_URL environment variable not defined")
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL")),
    }



# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

# STATIC_URL = 'static/'

STATIC_URL = '/static/'
STATIC_ROOT   = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
MEDIA_URL = '/media/'
MEDIA_ROOT   = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# custom absract user model
AUTH_USER_MODEL = 'users.User'

# whitenoise for serving static files
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Account auth settings

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_USER_MODEL_USERNAME_FIELD = None
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False


# change default date time format
DATETIME_FORMAT = 'Y-m-d H:M:S'


# Email config

# # django dev console smtp server
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# # gmail smtp server
# EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
# EMAIL_USE_TLS = True
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = "587"
# EMAIL_HOST_USER = "netrink18@gmail.com"
# EMAIL_HOST_PASSWORD = "lawvkzjdeaadaosa"

# titan mail smtp server
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_SSL = True
EMAIL_HOST = "smtp.titan.email"
EMAIL_PORT = "465"
EMAIL_HOST_USER = "support@netrink.com"
EMAIL_HOST_PASSWORD = "netrinkSupport66"
DEFAULT_FROM_EMAIL = 'support@netrink.com'
SERVER_EMAIL = 'support@netrink.com'


# CORS HEADERS
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True


# Rest framework settings

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication',],
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.IsAuthenticated',],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
}


# Djoser config

DOMAIN = 'www.netrink.com/#'
# DOMAIN = 'localhost:4200'
SITENAME = 'netRink'

DJOSER = {
    "LOGIN_FIELD": "email",
    "USER_CREATE_PASSWORD_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SET_USERNAME_RETYPE": True,
    "SET_PASSWORD_RETYPE": True,
    "SEND_ACTIVATION_EMAIL": True,
    "ACTIVATION_URL": "auth/activate?uid={uid}&token={token}",
    "PASSWORD_RESET_CONFIRM_URL": "auth/reset?uid={uid}&token={token}",
    "SERIALIZERS": { 
        'current_user': 'suites.personal.users.serializers.UserSerializer' 
    },
}
