DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework'
]

# External installed apps
EXTERNAL_APPS = [
    'webpack_loader'
]

# financial apps
INTERNAL_APPS = [
    'core'
]

APPS_SET = list(set(DJANGO_APPS + EXTERNAL_APPS +INTERNAL_APPS))