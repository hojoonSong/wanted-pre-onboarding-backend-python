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
    # 기본 설치 어플리케이션
]

MIDDLEWARE = [
    # 미들웨어 설정
]

ROOT_URLCONF = 'wanted.urls'

TEMPLATES = [
    # 템플릿 설정
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
