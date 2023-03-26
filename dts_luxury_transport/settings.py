"""
Django settings for dts_luxury_transport project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
import environ

# .env file that contains all api key credentials


env = environ.Env()
environ.Env.read_env() # Reads the .env file

# from dotenv import load_dotenv, find_dotenv

# load_dotenv(find_dotenv(".env"))


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-(k1a%_g^eoxtd0&2oxxtcku7qpit5^0=i$9n80k55-d@vi*=w5'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'users',
    'passenger',
    'user_base',
    #'sendgrid',
    'rentals',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'dts_luxury_transport.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'passenger/templates/'],
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

SESSION_ENGINE = 'django.contrib.sessions.backends.db'

WSGI_APPLICATION = 'dts_luxury_transport.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases
#Render PostgreSql Database (Live)
import dj_database_url
DATABASES = {
    'default': dj_database_url.parse(env('DATABASE_URL')),
}
# local database
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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

STRIPE_ENDPOINT_SECRET ='whsec_54a7d2ef3d504a421a08985a115ca58748787608201695fee4660a875b4db0c4'


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = 'passenger/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, "passenger/static/")]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

GOOGLE_API_KEY = "AIzaSyD4AxDzaud9qeLkEnrLCRJwrwZjeK6uA9E"

RECAPTCHA_PRIVATE_KEY = "6Lf4lMskAAAAAB1WEDR3WcFq-_i2CtB6_lcThMHa"
RECAPTCHA_PUBLIC_KEY = "6Lf4lMskAAAAANm9atQ62D_cvd8fJ1yU2VoUhFOD"

#RECAP ENTER 
#RECAP_SEC = "6Lf9ucQkAAAAAE9HdoHO2nIHXc19dywcQ69RvgrI"
#RECAP_PUB = "6Lf9ucQkAAAAAMgKUYs06FeiJmwhYYErwfef6FiC"

#images that are upload for the cars images
MEDIA_URL = '/media/'
MEDIA_ROOT = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

#user driver and passengers
LOGIN_URL = "users:sign-in"
LOGIN_REDIRECT_URL = "users:profile"
LOGOUT_REDIRECT_URL = "users:sign-in"

AUTH_USER_MODEL = 'user_base.UserBase'

BASE_COUNTRY = "UK"



# Twilio SendGrid

EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')

SENDGRID_API_KEY = env('SENDGRID_API_KEY')
FROM_EMAIL = env('FROM_EMAIL', default='noreply@gmail.com')

#EMAIL FOR CONTACT
CONTACT_EMAIL = env('CONTACT_EMAIL', default='noreply@gmail.com')
ADMIN_EMAILS = env('ADMIN_EMAILS', default='noreply@gmail.com')

#Jazzmin
JAZZMIN_SETTINGS = {
    "show_ui_builder": True
}

JAZZMIN_UI_TWEAKS = {
    #...
    "theme": "cerulean",
}

