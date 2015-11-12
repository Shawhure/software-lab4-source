#update for b3 id = 2
#update for C4 id = 2
import os  
BASE_DIR = os.path.dirname(os.path.dirname(__file__))  
import os.path   
import sae.const  
from os import environ  
debug = not environ.get("APP_NAME", "")   
if debug:  
    MYSQL_DB = 'pythondjangotest'      
    MYSQL_USER = 'shawhure'
    MYSQL_PASS = '19950423'
    MYSQL_HOST_M = '127.0.0.1'   
    MYSQL_HOST_S = '127.0.0.1'   
    MYSQL_PORT = '3306'   
else:   
    import sae.const   
    MYSQL_DB = sae.const.MYSQL_DB   
    MYSQL_USER = sae.const.MYSQL_USER   
    MYSQL_PASS = sae.const.MYSQL_PASS   
    MYSQL_HOST_M = sae.const.MYSQL_HOST   
    MYSQL_HOST_S = sae.const.MYSQL_HOST_S   
    MYSQL_PORT = sae.const.MYSQL_PORT  

debug = not environ.get("APP_NAME", "")   
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'k23ex54dmt696z8&0aafyrgj!x5$y1^8a46m6rh___33gbbmz+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["pickbooksup.sinaapp.com"]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
	'books',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'pickbooksup.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'pickbooksup.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', 
        'NAME': MYSQL_DB, 
        'USER': MYSQL_USER, 
        'PASSWORD': MYSQL_PASS, 
        'HOST': MYSQL_HOST_M, 
        'PORT': MYSQL_PORT, 
    }
}
# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'
