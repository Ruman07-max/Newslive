"""
Django settings for backend project.
"""

from pathlib import Path
import os
from decouple import config

# ---------------- BASE DIR ----------------
BASE_DIR = Path(__file__).resolve().parent.parent


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
    'cloudinary_storage',
    'cloudinary',

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


# ---------------- MEDIA FILES (CLOUDINARY) ----------------

CLOUDINARY_STORAGE = {
    'CLOUD_NAME': config('CLOUDINARY_CLOUD_NAME', default=''),
    'API_KEY': config('CLOUDINARY_API_KEY', default=''),
    'API_SECRET': config('CLOUDINARY_API_SECRET', default=''),
    'RESOURCE_TYPE': 'auto',
}
MEDIA_URL = '/media/'


# ---------------- STORAGES (Django 5.1+/6.0 New Format) ----------------

STORAGES = {
    "default": {
        "BACKEND": "cloudinary_storage.storage.MediaCloudinaryStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}


# ---------------- DEFAULT PK ----------------

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
# ---------------- LOGGING (Show errors in Render logs) ----------------

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'root': {
        'handlers': ['console'],
        'level': 'WARNING',
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },
    },
}