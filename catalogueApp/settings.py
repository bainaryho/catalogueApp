"""
Django settings for catalogueApp project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8==r9f!3n6ez)34%pl1^$ode$c8orx&q%qcsv((m()h)d^q*=$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


#디버그모드가 켜져있거나 테스트가 실행되는동안 적용되지 않습니다.
#사이트를 프로덕션 환경으로 이동하고 디버그를 False로 설정하면
# 이 설정에 도메인/호스트를 추가해야 사이트를 제공할 수 있습니다.
ALLOWED_HOSTS = [
    'localhost','127.0.0.1'
]


#모든 프로젝트에 대해 편집해야하는 설정입니다.
#이 설정은 사이트에서 활성화된 어플리케이션을 장고에 알려줍니다.
INSTALLED_APPS = [
    'django.contrib.admin',#관리사이트
    'django.contrib.auth',#인증프레임워크
    'django.contrib.contenttypes',#콘텐츠 유형처리를 위한 프레임워크
    'django.contrib.sessions',#세션 프레임워크
    'django.contrib.messages',#메시징 프레임워크
    'django.contrib.staticfiles',#정적파일 관리를 위한 프레임워크
    #여기까지 기본적인 장고 어플리케이션
]

#실행할 미들웨어를 포함하는 목록
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

#애플리케이션의 루트URL 패턴이 정의된 파이썬 모듈
ROOT_URLCONF = 'catalogueApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'catalogueApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

#사용할 모든 데이터베이스의 설정을 포함하는 딕셔너리
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
