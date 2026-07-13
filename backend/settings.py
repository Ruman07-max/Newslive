"""
Django settings for backend project.
"""

from pathlib import Path
import os
from decouple import config

# ---------------- BASE DIR ----------------
BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------- SECURITY ----------------
# ---------------- SECURITY ----------------
SECRET_KEY = config(
    "SECRET_KEY",
    default="django-insecure-CHANGE-THIS-IN-PRODUCTION"
)

DEBUG = config("DEBUG", default=False, cast=bool)

ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="127.0.0.1,localhost"
).split(",")
# ---------------- APPLICATIONS ----------------
INSTALLED_APPS = [

    # Django default
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party
    'rest_framework',
    'corsheaders',

    # Local app
    'news_app',
]


# ---------------- MIDDLEWARE ----------------
MIDDLEWARE = [

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',

    'django.middleware.common.CommonMiddleware',

    'django.middleware.csrf.CsrfViewMiddleware',

    'django.contrib.auth.middleware.AuthenticationMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',

    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ---------------- CORS SETTINGS ----------------

# React frontend ke liye
CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_CREDENTIALS = True



# ---------------- URL / TEMPLATES ----------------

ROOT_URLCONF = 'backend.urls'


TEMPLATES = [

    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',

        'DIRS': [
            BASE_DIR / 'project'
        ],

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


WSGI_APPLICATION = 'backend.wsgi.application'



# ---------------- DATABASE ----------------



import dj_database_url

DATABASES = {
    'default': dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
    )
}

# ---------------- PASSWORD VALIDATION ----------------

AUTH_PASSWORD_VALIDATORS = [

    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator'
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator'
    },

    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator'
    },

]



# ---------------- LANGUAGE / TIME ----------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True



# ---------------- STATIC FILES ----------------

STATIC_URL = '/static/'

STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'



# ---------------- MEDIA FILES ----------------

MEDIA_URL = '/media/'

MEDIA_ROOT = BASE_DIR / 'media'



# ---------------- DEFAULT PK ----------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'