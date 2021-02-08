from .base import *

import django_heroku

ALLOWED_HOSTS = ['artur-gorski-car-app.herokuapp.com']

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

django_heroku.settings(locals())
