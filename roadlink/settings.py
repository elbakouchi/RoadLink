"""
Django settings for roadlink project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import environ

ROOT_DIR = (
        environ.Path(__file__) - 2
)  # (bootcamp/config/settings/base.py - 3 = bootcamp/)
APPS_DIR = ROOT_DIR.path("")
# print(ROOT_DIR)
APP_DIRS = True

env = environ.Env()
env.read_env(str(ROOT_DIR.path(".env")))
# print(env)
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c7#-5a82#$p11h1itg3(e9591bms*)1$9x+#ed5%5pip6psm)&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '*']
DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django_adminlte',
    # 'account.apps.AccountConfig',
    'adminlte3',
    'adminlte3_theme',
    'driver.apps.DriverConfig',
    'home.apps.HomeConfig',
    'booking.apps.BookingConfig',
    'vehicle.apps.VehicleConfig',
    'repair.apps.RepairConfig',
    'report.apps.ReportConfig',
    'acquittance.apps.AcquittanceConfig',
    'crispy_forms',
    'requests',
    'geopy',

    'widget_tweaks',
    'material',
    'organism',
    'budget',
    'mission',
    'district',
    'provider',
    'import_export',
    'django_q',

]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
   # "whitenoise.middleware.WhiteNoiseMiddleware"
]

ROOT_URLCONF = 'roadlink.urls'

print("APPS_DIR", str(APPS_DIR.path("templates")))

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        "DIRS": [str(APPS_DIR.path("templates"))],
        #'APP_DIRS': True,

        'OPTIONS': {
            "loaders": [
                "django.template.loaders.filesystem.Loader",
                "django.template.loaders.app_directories.Loader",
            ],
            'context_processors': [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'roadlink.wsgi.application'
ASGI_APPLICATION = 'roadlink.asgi.application'

# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.sqlite3',
#        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#    }
# }

#DATABASES = {"default": env.db("DATABASE_URL")}
#DATABASES["default"]["ATOMIC_REQUESTS"] = True

"""
DATABASES = {
   'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'roadlink1',
        'USER': 'roadlinker',
        'PASSWORD': '*963.0258/',
        'HOST': '172.17.208.1',
        'PORT': '3306',
    }
}
"""
from urllib.parse import urlparse

# Parse the database URL
DATABASE_URL = os.environ.get('DATABASE_URL')
print(urlparse(DATABASE_URL).path[1:], urlparse(DATABASE_URL).username, urlparse(DATABASE_URL).password, urlparse(DATABASE_URL).hostname, urlparse(DATABASE_URL).port)
if DATABASE_URL:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': urlparse(DATABASE_URL).path[1:],
            'USER': urlparse(DATABASE_URL).username,
            'PASSWORD': urlparse(DATABASE_URL).password,
            'HOST': urlparse(DATABASE_URL).hostname,
            'PORT': urlparse(DATABASE_URL).port,
        }
    }
else:
    raise ValueError("DATABASE_URL environment variable not set")

# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'fr-fr'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_ROOT = str(ROOT_DIR("staticfiles"))

STATIC_URL = '/static/'

STATICFILES_DIRS = [str(APPS_DIR.path("static"))]

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = 'roadlink/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'roadlink/media')

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'email'
EMAIL_HOST_PASSWORD = 'pass'
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

#STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"


Q_CLUSTER = {
    'name': 'RoadLink',
    'workers': 8,
    'timeout': 60,
    'orm': 'default',
    'broker_class': 'roadlink.broker.RoadLinkBroker'
}


LANGUAGES = [
    ('en', 'English'),
    ('fr', 'Français'),
]

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale'),
]

