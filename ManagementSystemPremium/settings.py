"""
Django settings for ManagementSystemPremium project.

Generated by 'django-admin startproject' using Django 3.1.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '^gj4*l7^c75mhlsrgmby=!!ro^%2%+2o41sg)hh0r=qe$k&tqd'

# SECURITY WARNING: don't run with debug turned on in production!

online = False
# SECURITY WARNING: don't run with debug turned on in production!
# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

if online:
    DEBUG = False
    ALLOWED_HOSTS = ['teamworkad.pythonanywhere.com']
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': "teamworkad$default",
            'USER': 'teamworkad',
            'PASSWORD': 'zjss123456',
            'HOST': 'teamworkad.mysql.pythonanywhere-services.com',
        }
    }
else:
    DEBUG = True
    ALLOWED_HOSTS = []
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }


# Application definition
INSTALLED_APPS = [
    'simpleui',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'notifications',
    'notice',
    'user',
    'team',
    'asset',
    'cost',
    'downgrade',
    'performance',
    'person',
    'reward',
    'sale',
    'service',
    'training',
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

ROOT_URLCONF = 'ManagementSystemPremium.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'user', 'templates'),
            os.path.join(BASE_DIR, 'performance', 'templates'),
            os.path.join(BASE_DIR, 'person', 'templates'),
            os.path.join(BASE_DIR, 'cost', 'templates'),
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

WSGI_APPLICATION = 'ManagementSystemPremium.wsgi.application'


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static', 'ManagementSystemPremium'),
    os.path.join(BASE_DIR, 'performance', 'static', 'performance'),
]

AUTH_USER_MODEL = 'user.CustomUser'

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"  # Default
EMAIL_HOST = "smtp.qq.com"
EMAIL_PORT = 25
EMAIL_HOST_USER = "xxx@qq.com"   # 邮箱
EMAIL_HOST_PASSWORD = "vtfkyizuxeysbeif"   # 邮箱授权码
EMAIL_USE_TLS = True
EMAIL_FROM = "xxx@qq.com"  # 邮箱

SIMPLEUI_HOME_INFO = False
SIMPLEUI_LOGO = ''

# SIMPLEUI_CONFIG = {
#     'system_keep': True,  # 关闭系统默认
#
#     # 菜单名
#     'menu_display': ['添加模块一', '测试用户信息', '添加模块二'],
#     'dynamic': True,  # 设置是否开启动态菜单, 默认为False. 如果开启, 则会在每次用户登陆时动态展示菜单内容
#
#     'menus': [
#         {
#             'name': '添加模块一',
#             'icon': 'fas fa-code',
#             'url': 'https://baidu.com'
#         },
#
#         {
#             'name': '测试用户信息',
#             'icon': 'fas fa-user-shield',
#             'models': [
#                 {
#                     'name': '用户信息',
#                     'icon': 'fa fa-user',
#                     # 渲染数据表菜单
#                     'url': '/admin/database/userinfo/'
#                 }
#             ]
#         },
#
#         {
#             'app': 'auth',
#             'name': '添加模块二',
#             'icon': 'fas fa-user-shield',
#             'models': [
#                 {
#                     'name': '用户',
#                     'icon': 'fa fa-user',
#                     'url': 'auth/user/'
#                 }
#             ]
#         },
#
#     ]
# }
