from .base import *
import os
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': BASE_DIR / 'db.sqlite3',
    # }
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'abuzahrah02'),
        'USER': os.environ.get('DB_USER', 'abuzahrah'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'zahrah@75'),
        'HOST': os.environ.get('DB_HOST', '165.22.63.162'),
        'PORT': os.environ.get('DB_PORT', '8107'),
    },
}
