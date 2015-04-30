"""
Django settings for CCPortal project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

sys.path.append(os.path.join(BASE_DIR, 'portal/portlets'))
 
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'JG1VCh9FFMRA9XpLQMapC6e1Xh4lFMmJ14me2lDjpAe3F9cJOY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = ['localhost', '178.62.46.211']


# Application definition

INSTALLED_APPS = (
    
    'menu',
    #'django_sockjs_tornado',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'social.apps.django_app.default',

    
    # Coffee Cup Apps
    'portal',
    'portal.site',
    'portal.portlets.dashboard',
    'portal.portlets.equipmentmanager',
    'portal.portlets.investorbulletin',
    'portal.portlets.locationmanager',
    'portal.portlets.mediasharing',
    #'portal.portlets.messenger',
    'portal.portlets.scheduling',
    'portal.portlets.useradministration',
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
                  
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'apptemplates.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
   'social.backends.facebook.FacebookOAuth2',
   'social.backends.google.GoogleOAuth2',
   'social.backends.twitter.TwitterOAuth',
   'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_USER_MODEL = 'site.User'

# SOCIAL_AUTH_FACEBOOK_KEY = '618381151630752' # REAL APP
# SOCIAL_AUTH_FACEBOOK_SECRET ='24c0544787dd08bf68468da58b35d00d' # REAL APP

SOCIAL_AUTH_FACEBOOK_KEY = '620204744781726' # TEST APP
SOCIAL_AUTH_FACEBOOK_SECRET ='eece66a9895a89fe781c9d68fceb58b0' # TEST APP

# FACEBOOK_EXTENDED_PERMISSIONS = ['email']
# SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True

LOGIN_REDIRECT_URL = '/'

ROOT_URLCONF = 'portal.urls'

WSGI_APPLICATION = 'portal.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django',
        'USER': 'django',
        'PASSWORD': 'dVhixvZPhM',
        'HOST': 'localhost',
        'PORT': '',
    }
}


SOCKJS_PORT = 9999
SOCKJS_CHANNEL = 'messenger'

SOCKJS_CLASSES = (
    'portal.portlets.messenger.sock.MessengerConnection',
)

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

MENU_SELECT_PARENTS = True

AUTH_USER_MODEL = 'site.User'

SITE_NAME = "coffeecup"

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = "./sitestatic/"

MEDIA_ROOT = './sitemedia/'
MEDIA_URL = '/media/'

