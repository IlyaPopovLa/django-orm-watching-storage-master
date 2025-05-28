import os
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured

load_dotenv()


def str_to_bool(value):
    return str(value).strip().lower() in ('1', 'true', 'yes')


DB_NAME = os.getenv('DB_NAME')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
SECRET_KEY = os.getenv('SECRET_KEY')

if not DB_NAME:
    raise ImproperlyConfigured("Не указан DB_NAME.")
if not DB_USER:
    raise ImproperlyConfigured("Не указан DB_USER.")
if not DB_PASSWORD:
    raise ImproperlyConfigured("Не указан DB_PASSWORD.")
if not SECRET_KEY:
    raise ImproperlyConfigured("Не указан SECRET_KEY.")


DB_ENGINE = os.getenv('DB_ENGINE', 'django.db.backends.postgresql_psycopg2')
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')

DEBUG = str_to_bool(os.getenv('DEBUG', 'False'))

raw_hosts = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost')
ALLOWED_HOSTS = [host.strip() for host in raw_hosts.split(',') if host.strip()]

if not DEBUG and ALLOWED_HOSTS == ['127.0.0.1', 'localhost']:
    raise ImproperlyConfigured("Укажите ALLOWED_HOSTS")

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
    }
}

INSTALLED_APPS = ['datacenter']
ROOT_URLCONF = 'project.urls'

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]

LANGUAGE_CODE = 'ru-ru'
TIME_ZONE = 'Europe/Moscow'
USE_TZ = True
USE_L10N = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
