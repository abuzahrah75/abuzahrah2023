from .base import *
import os
# SECURITY WARNING: don't run with debug turned on in production!/
DEBUG = True
# DEBUG = bool(os.environ.get('DJANGO_DEBUG', True))
ALLOWED_HOSTS = ["abuzahrah.com"]

DATABASES = {

        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': os.environ.get('DB_NAME', 'mydatabase'),
            'USER': os.environ.get('DB_USER', 'mydatabaseuser'),
            'PASSWORD': os.environ.get('DB_PASSWORD', 'mypassword'),
            'HOST': os.environ.get('DB_HOST', '127.0.0.1'),
            'PORT': os.environ.get('DB_PORT', '5432'),
        },
}
