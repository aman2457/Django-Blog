from mysite.settings.common import *


SECRET_KEY = '4tj^^^9)w1ud)#(2_%k_364srrp79weag)qzud2%k19^961h$^'
# SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY','4tj^^^9)w1ud)#(2_%k_364srrp79weag)qzud2%k19^961h$^')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']


EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'
EMAIL_PORT = 587
