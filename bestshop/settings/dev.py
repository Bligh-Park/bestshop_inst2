from .base import *

DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'test',
        'USER': 'Bligh',
        'PASSWORD': 'bligh1212',
        'HOST': 'bestshop.c9sffsfurh2l.us-west-2.rds.amazonaws.com',
        'PORT': '5432',
    }
}
