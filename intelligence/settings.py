"""
Django settings for intelligence project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&ug=2p3t^x+&!9vt*kjr--g-)ta5=o)4@v&6ks-w#k69nl+v$k'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '.apps.kepcodevops.openshift.com'
]


# Application definition

INSTALLED_APPS = [
    'apps.reputation.apps.ReputationConfig',
    'apps.twitter.apps.TwitterConfig',
    'apps.twitter_hunter.apps.TwitterHunterConfig',
    'apps.exploit.apps.ExploitConfig',
    'apps.threat.apps.ThreatConfig',
    'apps.threat_hunter.apps.ThreatHunterConfig',
    'apps.dashboard.apps.DashboardConfig',
    'apps.domain.apps.DomainConfig',
    'apps.ip.apps.IpConfig',
    'apps.filehash.apps.FilehashConfig',
    'apps.url.apps.UrlConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'pure_pagination',
    'rest_framework',
    'django_filters',
    'bootstrap4',
    'django_celery_results',
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

ROOT_URLCONF = 'intelligence.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'libraries':{
                'lookup': 'apps.reputation.templatetags.lookup',
                }
        },
    },
]

WSGI_APPLICATION = 'intelligence.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'intelligence_db',
        'USER': 'exist',
        'PASSWORD': 'Passw0rd',
        'HOST': 'exist-mariadb',
        'PORT': '3306',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': 'SET character_set_connection=utf8mb4;'
                            'SET collation_connection=utf8mb4_unicode_ci;'
                            "SET NAMES 'utf8mb4';"
                            "SET CHARACTER SET utf8mb4;"
        },
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static/"),
)

#STATIC_ROOT = os.path.join(BASE_DIR, "static-root/")

# for django-pure-pagination settings
PAGINATION_SETTINGS = {
    'PAGE_RANGE_DISPLAYED': 2,
    'MARGIN_PAGES_DISPLAYED': 2,

    'SHOW_FIRST_PAGE_WHEN_INVALID': True,
}

# format
FORMAT_MODULE_PATH = 'intelligence.formats'

# Rest API
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50,
}

# intcomma
NUMBER_GROUPING = 3

# Celery
CELERY_RESULT_BACKEND = 'django-db'

# Logging
LOGGING = {
    'version': 1,
    'formatters': {
        'all': {
            'format': '\t'.join([
                "[%(levelname)s]",
                "%(asctime)s",
                "module:%(module)s",
                "%(pathname)s",
                "message:%(message)s",
            ])
        },
        'django.server': {
            '()': 'django.utils.log.ServerFormatter',
            'format': '%(asctime)s %(message)s',
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'logs/django.log'),
            'formatter': 'all',
            'maxBytes': 1024 * 1024 * 2,
            'backupCount': 10,
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler', 
            'formatter': 'all'
        },
        'django.server': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'django.server',
        },
    },
    'loggers': {
        'command': {
            'handlers': ['file', 'console'],
            'level': 'DEBUG',
        },
        'django.server': {
            'handlers': ['django.server'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}
