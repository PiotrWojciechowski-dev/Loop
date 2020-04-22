"""
Django settings for Loop project.

Generated by 'django-admin startproject' using Django 2.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'us72an53yf4bk8p0b!1#dhmnr2*^_vghq!o=bib^4mo6hhkc48'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'admin_shortcuts' ,
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'user.apps.UserConfig',
    'post.apps.PostConfig',
    'search.apps.SearchConfig',
    'profiles.apps.ProfilesConfig',
    'likes.apps.LikesConfig',
    'private_messages.apps.PrivateMessagesConfig',
    'shop.apps.ShopConfig',
    'cart.apps.CartConfig',
    'order.apps.OrderConfig',
    #'imagekit',
    'crispy_forms',
    'django_countries',
    'django_filters',
    'paypal.standard.ipn',
    'stripe',
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

ROOT_URLCONF = 'Loop.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),os.path.join(BASE_DIR, 'post', 'templates/'),
                                                    os.path.join(BASE_DIR, 'user', 'templates/'),
                                                    os.path.join(BASE_DIR, 'search', 'templates/'),
                                                    os.path.join(BASE_DIR, 'profiles', 'templates/'),
                                                    os.path.join(BASE_DIR, 'shop', 'templates/'),
                                                    os.path.join(BASE_DIR, 'cart', 'templates/'),
                                                    os.path.join(BASE_DIR, 'order', 'templates/'),
                                                    ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
                'cart.context_processors.cart',
            ],
        },
    },
]

AUTH_USER_MODEL = 'user.CustomUser'

AUTHENTICATION_BACKENDS = [
    ('django.contrib.auth.backends.ModelBackend'),
]
WSGI_APPLICATION = 'Loop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/London'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

# Static Files Configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

# User Files Configuration
LOGIN_URL= '/signin/'
LOGIN_REDIRECT_URL = 'home'

# Media Files Configuration
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# File Storage Configuration
#DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

# Admin Configuration
ADMIN_SHORTCUTS = [
    {
        'shortcuts': [
            { 
                'title': 'Home Page',     
                'url': '/',
                'open_new_window': True,
            },
            {
                'url_name': 'admin:logout',
            },
            {
                'title': 'Index',
                'url_name': 'admin:index',
            },
            {
                'title': 'Users',
                'url_name': 'admin:user_customuser_changelist',
                'count': 'user.utils.count_users',
            },
            {
                'title': 'Groups',
                'url_name': 'admin:auth_group_changelist',
                'count': 'user.utils.count_groups',
            },
            {
                'title': 'Add user',
                'url_name': 'admin:user_customuser_add',
                'has_perms': 'example.utils.has_perms_to_users',
            },
        ]
    },
    {
        'title': 'Quick Acess',
        'shortcuts': [
            {
                'title': 'Products',
                'url_name': 'admin:shop_product_changelist',
            },
            {
                'title': 'Orders',
                'url_name': 'admin:order_order_changelist',
                'count': '',
            },
        ]
    },
]

ADMIN_SHORTCUTS_SETTINGS = {
    'show_on_all_pages': True,
    'hide_app_list': False,
    'open_new_window': False,
}

# Other Files Configuration
CRISPY_TEMPLATE_PACK = 'bootstrap4'

CART_SESSION_ID = 'cart'

#django-paypal settings
PAYPAL_RECEIVER_EMAIL = 'x00154002@mytudublin.ie'
PAYPAL_TEST = True

#django-stripe keys
STRIPE_SECRET_KEY = 'sk_test_6umaOLKEqvEpQEyCPrHO73U100CTgwZNE8'
STRIPE_PUBLISHABLE_KEY = 'pk_test_qBVMPqWOiLNRYgzNowY4zBnE004YK6BQRC'
