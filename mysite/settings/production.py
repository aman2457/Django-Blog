from mysite.settings.common import *
import dj_database_url

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','4tj^^^9)w1ud)#(2_%k_364srrp79weag)qzud2%k19^961h$^')

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = False
DEBUG = os.environ.get('DJANGO_DEBUG', '') != 'False'
