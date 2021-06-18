from .base import *
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'guakamaya',
        'USER': 'jcjohan',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}