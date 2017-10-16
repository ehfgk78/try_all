"""
Django settings for try_all project.

Generated by 'django-admin startproject' using Django 1.11.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""
import json
import os

# ~/projects/django/djangoTryAll/try_all
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
####### 장고 key와 DB pw 등을 배포와 git으로부터 노출되지 않게 하기 ################
# 4. .gitignore에 .config_secret/ 폴더를 추가
# 목적:  djangoTryAll/.config_secret/settings_common.json에 접근하기
ROOT_DIR = os.path.dirname(BASE_DIR)
SETTINGS_COMMON_JSON = os.path.join(os.path.join(ROOT_DIR, '.config_secret'), 'settings_common.json')

with open(SETTINGS_COMMON_JSON) as f:
    settings_common_json = f.read()
settings_common_dict = json.loads(settings_common_json)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = settings_common_dict["django"]["secret_key"]
# 템플릿파일을 저장할 'templates'폴더
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_URL = '/static/'
# 정적파일을 저장할 'static'폴더
STATIC_DIR = os.path.join(BASE_DIR, 'static')
# Django에서 정적파일을 검색하고 가져올 폴더 목록
STATICFILES_DIR = [ STATIC_DIR, ]


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    '*',
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # 3rd-party applications
    'django_extensions',

    # User applications
    'blog',
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

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            TEMPLATE_DIR,
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

WSGI_APPLICATION = 'config.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = settings_common_dict['django']['databases']

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

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


