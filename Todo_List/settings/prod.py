import django_on_heroku
from decouple import config

from .settings import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    'sunitha-todo-list.herokuapp.com',
    'sunitha.base',
]

DEBUG_PROPAGATE_EXCETIONS = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%d/%b/%Y %H:%M:%S"
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.Streamandler',
        },
    },
    'loggers': {
        'MYAPP': {
            'handlers': ['console'],
            'level': 'DEBUG',
        },
    }
}
#Heroku Settings
django_on_heroku.settings(locals(), staticfiles=False)
del DATABASES['default']['OPTIONS']['sslmode']