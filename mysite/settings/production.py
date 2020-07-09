from mysite.settings.common import *
import dj_database_url
from decouple import config,csv

#SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY',)

# SECURITY WARNING: don't run with debug turned on in production!

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', cast=bool)
#DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'

ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_NAME'),
        'USER': config('DB_USER'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': '',
    }
}

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = config('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
EMAIL_PORT = 587

db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)