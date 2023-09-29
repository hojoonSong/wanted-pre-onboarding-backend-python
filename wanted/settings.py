import os
from dotenv import load_dotenv
from pathlib import Path

# 환경 변수 로드
load_dotenv()

# 프로젝트 기본 디렉토리 설정
BASE_DIR = Path(__file__).resolve().parent.parent

# 보안 경고: 실제 프로덕션에서는 Secret Key를 비밀로 유지하세요!
SECRET_KEY = os.getenv('SECRET_KEY')

# 보안 경고: 실제 프로덕션에서는 Debug를 False로 설정하세요!
DEBUG = os.getenv('DEBUG') == 'True'

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')

# 어플리케이션 정의
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',  # 인증 및 권한을 관리하는 앱
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # 세션 관리를 위한 앱
    'django.contrib.messages',  # 메시징 프레임워크
    'django.contrib.staticfiles',  # 정적 파일을 관리하는 앱
    'rest_framework',
    'wanted.jobpostings',
]

MIDDLEWARE = [
    # ...
    'django.contrib.sessions.middleware.SessionMiddleware',  # 이 라인을 추가합니다.
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 이 라인이 이미 존재한다면, 위치를 확인해주세요.
    'django.contrib.messages.middleware.MessageMiddleware',  # 이 라인을 추가합니다.
    # ...
]

ROOT_URLCONF = 'wanted.urls'

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

WSGI_APPLICATION = 'wanted.wsgi.application'

# 데이터베이스 설정
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}

# 비밀번호 검증
AUTH_PASSWORD_VALIDATORS = [
    # 비밀번호 검증 설정
]


# 국제화
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# 정적 파일 (CSS, JavaScript, Images)
STATIC_URL = 'static/'

# 기본 프라이머리 키 필드 유형
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
