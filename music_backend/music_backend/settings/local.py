from .base import *
import os
from dotenv import load_dotenv
# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'winamp',
        'USER': 'postgres',
        'PASSWORD': 'password123',
        'HOST': 'localhost',
        'PORT': ''
    }
}
