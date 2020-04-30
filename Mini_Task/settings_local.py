from Mini_Task.settings import *

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'banners',
        'USER': 'data',
        'PASSWORD': 'chef',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
