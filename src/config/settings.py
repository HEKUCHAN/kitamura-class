import os
import environ
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, ".env"))


def env_list(some):
    if isinstance(some, list):
        return some
    else:
        return some.replace("[", "").replace("]", "").split(",")


def env_bool(some):
    if isinstance(some, bool):
        return some
    else:
        return bool(some)

print("############### ENV INFO ##############")

SECRET_KEY = os.getenv("SECRET_KEY", env.get_value("SECRET_KEY", str))
print("SECRET_KEY:", "LOADED")

DEBUG = env_bool(os.getenv("DEBUG", env.bool("DEBUG", default=False)))
print("DEBUG:", DEBUG)

ALLOWED_HOSTS = env_list(os.getenv("ALLOWED_HOSTS", env.list("ALLOWED_HOSTS")))
print("ALLOWED_HOSTS:")
for allowed_host in ALLOWED_HOSTS:
    print("    ", allowed_host)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "corsheaders",
    "calc_bmi"
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


DATABASES = {
    "default": {
        "ENGINE": os.getenv("DB_ENGINE", env.get_value("DB_ENGINE", str)),
        "NAME": "kitamura_db",
        "USER": os.getenv("DB_USER", env.get_value("DB_USER", str)),
        "PASSWORD": os.getenv("DB_PASSWORD", env.get_value("DB_PASSWORD", str)),
        "PORT": os.getenv("DB_PORT", env.get_value("DB_PORT", str)),
        "HOST": os.getenv("DB_HOST", env.get_value("DB_HOST", str)),
        "TEST": {
            "NAME": "test_kitamura_db",
        },
    }
}

DATABASE_INFO = DATABASES["default"]

print("############ DATABASE INFO ############")
print("ENGINE:" , DATABASE_INFO["ENGINE"])
print("NAME:", DATABASE_INFO["NAME"])
print("DB_USER:", DATABASE_INFO["USER"])
print("PORT:", DATABASE_INFO["PORT"])
print("HOST:", DATABASE_INFO["HOST"])
print("#######################################")

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ja'

TIME_ZONE = 'Asia/Tokyo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
