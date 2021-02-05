from .base import *

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

INTERNAL_IPS = ('127.0.0.1', 'localhost', '0.0.0.0')


def show_toolbar(request):
    if request.is_ajax():
        return False
    return True


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': 'config.settings.dev.show_toolbar',
}
