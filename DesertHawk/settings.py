"""
Django settings for DesertHawk project.

Generated by 'django-admin startproject' using Django 2.2.12.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""
import datetime
import decimal
import json
import os

import logging  # 引入logging模块

from qcloud_cos import CosConfig, CosS3Client

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(filename)s [line:%(lineno)d] - %(levelname)s: %(message)s')

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import time

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '05duh!gv&6^1(8r-76#ne%(taue_!+4dye2dqb*7e24(-ywq%&'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
X_FRAME_OPTIONS = 'SAMEORIGIN'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'ckeditor',
    'ckeditor_uploader',
    'apps.aboutme',
    'apps.statistic',
    'apps.articles',
    'apps.articles.program',
    'apps.articles.travel',
    'apps.user',
    'apps.home',
    'apps.comment',
    'apps.gbook',
    'apps.search',
    'apps.document',
    'apps.administrator',
    'libs.mdeditor',
    'DesertHawk',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'DesertHawk.urls'
START_TIME = time.time()

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'apps'),
                 os.path.join(BASE_DIR, 'apps/articles/program'),
                 os.path.join(BASE_DIR, 'apps/comment'),
                 os.path.join(BASE_DIR, 'apps/user'),
                 os.path.join(BASE_DIR, 'apps/gbook'),
                 os.path.join(BASE_DIR, 'apps/aboutme'),
                 os.path.join(BASE_DIR, 'apps/search'),
                 ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',  # 在模板中可以使用{{ Media——URL}}
                'DesertHawk.context_processors.theme',  # 在模板中可以使用{{ Media——URL}}
                'DesertHawk.context_processors.visit_count',
            ],
        },
    },
]

WSGI_APPLICATION = 'DesertHawk.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'zhqiBlog',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        'PORT': '3306'
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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

CKEDITOR_CONFIGS = {
    'default': {
        'width': 'auto',
        'tabSpaces': 4,
        'extraPlugins': 'codesnippet',
        'toolbar': (['div', 'Source', '-', 'Save', 'NewPage', 'Preview', '-', 'Templates'],
                    ['Cut', 'Copy', 'Paste','PasteText','PasteFromWord', '-', 'Print', 'SpellChecker', 'Scayt'],
                    ['Undo', 'Redo', '-', 'Find', 'Replace', '-', 'SelectAll','RemoveFormat'],
                    ['Form', 'Checkbox', 'Radio', 'TextField', 'Textarea','Select', 'Button', 'ImageButton', 'HiddenField'],
                    ['Bold', 'Italic', 'Underline', 'Strike', '-', 'Subscript', 'Superscript'],
                    ['NumberedList', 'BulletedList', '-', 'Outdent', 'Indent', 'Blockquote'],
                    ['JustifyLeft', 'JustifyCenter', 'JustifyRight', 'JustifyBlock'],
                    ['Link', 'Unlink', 'Anchor'],
                    ['Image', 'Flash', 'Table', 'HorizontalRule', 'Smiley', 'SpecialChar', 'PageBreak'],
                    ['Styles', 'Format', 'Font','FontSize'],
                    ['TextColor', 'BGColor'],
                    ['Maximize', 'ShowBlocks', '-', 'About', 'pbckcode'],
                    ['CodeSnippet'],
                    ),
    }
}

MDEDITOR_CONFIGS = {
    'default': {
        'width': '90%',  # 自定义编辑框宽度
        'heigth': 500,  # 自定义编辑框高度
        'toolbar': ["undo", "redo", "|",
                    "bold", "del", "italic", "quote", "ucwords", "uppercase", "lowercase", "|",
                    "h1", "h2", "h3", "h5", "h6", "|",
                    "list-ul", "list-ol", "hr", "|",
                    "link", "reference-link", "image", "code", "preformatted-text", "code-block", "table", "datetime",
                    "emoji", "html-entities", "pagebreak", "goto-line", "|",
                    "help", "info",
                    "||", "preview", "watch", "fullscreen"],  # 自定义编辑框工具栏
        'upload_image_formats': ["jpg", "jpeg", "gif", "png", "bmp", "webp"],  # 图片上传格式类型
        'image_floder': 'editor',  # 图片保存文件夹名称
        'theme': 'gray',  # 编辑框主题 ，dark / default
        'preview_theme': 'default',  # 预览区域主题， dark / default
        'editor_theme': 'pastel-on-dark',  # edit区域主题，pastel-on-dark / default
        'toolbar_autofixed': True,  # 工具栏是否吸顶
        'search_replace': True,  # 是否开启查找替换
        'emoji': True,  # 是否开启表情功能
        'tex': True,  # 是否开启 tex 图表功能
        'flow_chart': True,  # 是否开启流程图功能
        'lineWrapping': True,
        'lineNumbers': True,
        'watch': True,
        'sequence': True  # 是否开启序列图功能
    }
}

# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'zh-hans'
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), os.path.join(BASE_DIR, 'libs')]

BLOG_ROOT = './'
THEME = "white"
MEDIA_URL = '/media/'
THUMB_URL = '/articles/thumb/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
CKEDITOR_UPLOAD_PATH = ""

IMAGES_URL = '/images/'
CKEDITOR_STORAGE_BACKEND = 'DesertHawk.view.StorageObject'  # 自定义ckedit上传路径
MKEDITOR_STORAGE_BACKEND = 'DesertHawk.view.StorageObject'  # 自定义ckedit上传路径

secret_id = os.environ["COS_SECRET_ID"]
secret_key = os.environ["COS_SECRET_KEY"]

sms_app_id = os.environ["SMS_APP_ID"]
sms_app_key = os.environ["SMS_APP_KEY"]

region = 'ap-beijing'  # 替换为用户的 Region
token = None  # 使用临时密钥需要传入 Token，默认为空，可不填
scheme = 'http'  # 指定使用 http/https 协议来访问 COS，默认为 https，可不填
config = CosConfig(Region=region, SecretId=secret_id, SecretKey=secret_key, Token=token, Scheme=scheme)
# 2. 获取客户端对象
cos_client = CosS3Client(config)


class JsonCustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return float(obj)
        elif isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)