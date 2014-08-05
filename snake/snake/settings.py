"""
Django settings for snake project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import AUTH_USER_MODEL

SITE_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

BASE_DIR = os.path.dirname(os.path.dirname(__file__))



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3gusq#+b*mis*cb7=6pg^=3%au&yyd4!zsz!oe1k#wrn9i09_2'

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
	'south',
	'game',
	'registration',
	'bcrypt',
)

MIDDLEWARE_CLASSES = (
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'snake.urls'

WSGI_APPLICATION = 'snake.wsgi.application'

# PASSWORD HASHERS

PASSWORD_HASHERS = (
	'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
	'django.contrib.auth.hashers.BCryptPasswordHasher',
	'django.contrib.auth.hashers.PBKDF2PasswordHasher',
	'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
	'django.contrib.auth.hashers.SHA1PasswordHasher',
	'django.contrib.auth.hashers.MD5PasswordHasher',
	'django.contrib.auth.hashers.CryptPasswordHasher',
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


PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

STATIC_URL = '/static/'

MEDIA_URL = '/media/'

LOGIN_REDIRECT_URL = '/'

ACCOUNT_ACTIVATION_DAYS = 7
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'Djangorockstar@gmail.com'
EMAIL_HOST_PASSWORD = 'Djangorockstar#123'

AUTH_PROFILE_MODULE = 'registration.RegistrationProfile'

TEMPLATE_DIRS = (
	os.path.join(SITE_ROOT, "templates"),
)

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, "static", "static"),
)

MEDIA_ROOT = os.path.join(BASE_DIR, 'static', 'media')

try:
	from local_settings import *
except ImportError:
	pass
