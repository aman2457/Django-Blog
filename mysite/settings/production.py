from mysite.settings.common import *
import dj_database_url

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','4tj^^^9)w1ud)#(2_%k_364srrp79weag)qzud2%k19^961h$^')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']



DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'aapanbihar',
        'USER': 'name',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '',
    }
}


db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)