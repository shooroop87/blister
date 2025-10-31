# config/settings.py - ИСПРАВЛЕНА СТРУКТУРА ШАБЛОНОВ
import io
import os
import sys
from pathlib import Path

from django.utils.translation import gettext_lazy as _
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv("SECRET_KEY", "1insecure1-1default1")

# DEBUG выключает все виды кэша и сжатия
DEBUG = True

# ALLOWED_HOSTS
if DEBUG:
    ALLOWED_HOSTS = ["*"]
else:
    ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost 127.0.0.1").split()

CSRF_TRUSTED_ORIGINS = [
    "http://localhost",
    "http://localhost:8000",
    "http://backend-1:8000",
    "http://127.0.0.1",
    "http://127.0.0.1:8000",
    "http://0.0.0.0:8000",
]

# Приложения
INSTALLED_APPS = [
    # Django
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 3rd party
    "easy_thumbnails",
    "filer",
    "mptt",
    "parler",
    "taggit",
    "meta",
    "tinymce",
    "core",
]
# Работает в связке с django.contrib.sites
# SITE_ID = 1

# Dev-only apps
if DEBUG:
    INSTALLED_APPS += ["django_browser_reload"]

MIDDLEWARE = [
    "django.middleware.gzip.GZipMiddleware",
    "django.middleware.security.SecurityMiddleware",
    # "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
if DEBUG:
    MIDDLEWARE.append("django_browser_reload.middleware.BrowserReloadMiddleware")

ROOT_URLCONF = "config.urls"

TEMPLATES_DIR = BASE_DIR / "templates"
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            BASE_DIR / "core" / "templates",  # Основные шаблоны
            BASE_DIR / "templates",  # Общие шаблоны
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"

# PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

DEFAULT_CHARSET = "utf-8"
FILE_CHARSET = "utf-8"

LANGUAGE_CODE = "en"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

LANGUAGES = [
    ("en", "English"),
]

LOCALE_PATHS = [BASE_DIR / "core" / "locale"]

# Static & media
STATIC_URL = "/static/"
STATICFILES_DIRS = [BASE_DIR / "core" / "static"]
STATIC_ROOT = BASE_DIR / "collected_static"

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

FILE_UPLOAD_PERMISSIONS = 0o644  # rw-r--r--
FILE_UPLOAD_DIRECTORY_PERMISSIONS = 0o755  # rwxr-xr-x

# Создаем медиа-директорию если не существует
os.makedirs(MEDIA_ROOT, exist_ok=True)

# Filer / thumbnails
THUMBNAIL_HIGH_RESOLUTION = True
THUMBNAIL_QUALITY = 90
THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "easy_thumbnails.processors.scale_and_crop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters",
)

# Отключить строгий режи
# WHITENOISE_MANIFEST_STRICT = False

# Cache / static storages
if DEBUG:
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
    CACHES = {"default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"}}
else:
    # STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    STATICFILES_STORAGE = "django.contrib.staticfiles.storage.StaticFilesStorage"
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": os.getenv("REDIS_URL", "redis://redis:6379/1"),
            "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        }
    }

# НОВОЕ: Настройки для принуждения обновления браузерного кеша
# STATIC_CACHE_CONTROL = "public, max-age=3600"  # 1 час вместо года

# Email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = os.getenv("EMAIL_HOST", "your-smtp-server.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))
EMAIL_USE_TLS = os.getenv("EMAIL_USE_TLS", "True").lower() == "true"
EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "your-email@domain.com")
EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASSWORD", "your-password")
DEFAULT_FROM_EMAIL = "Abroads Tours <noreply@blisterbox.com>"
CONTACT_EMAIL = "abroadstour@gmail.com"

# Контакты
CONTACT_PHONE = "+39-339-2168555"
WHATSAPP_NUMBER = "393392168555"

# SendPulse
SENDPULSE_API_USER_ID = os.getenv("SENDPULSE_API_USER_ID", "your-user-id")
SENDPULSE_API_SECRET = os.getenv("SENDPULSE_API_SECRET", "your-secret")
SENDPULSE_ADDRESS_BOOK_ID = os.getenv("SENDPULSE_ADDRESS_BOOK_ID", "your-book-id")

# SEO / verification
GOOGLE_ANALYTICS_ID = os.getenv("GA_MEASUREMENT_ID", "GA_MEASUREMENT_ID")
YANDEX_METRICA_ID = os.getenv("YANDEX_METRICA_ID", "YOUR_YANDEX_ID")
BING_WEBMASTER_ID = os.getenv("BING_WEBMASTER_ID", "YOUR_BING_ID")
BING_UET_TAG = os.getenv("BING_UET_TAG", "YOUR_BING_UET_TAG")
GOOGLE_SITE_VERIFICATION = os.getenv("GOOGLE_SITE_VERIFICATION", "")
YANDEX_VERIFICATION = os.getenv("YANDEX_VERIFICATION", "")
BING_SITE_VERIFICATION = os.getenv("BING_SITE_VERIFICATION", "")

# hCaptcha
HCAPTCHA_SITEKEY = os.getenv("HCAPTCHA_SITEKEY", "your-site-key-here")
HCAPTCHA_SECRET = os.getenv("HCAPTCHA_SECRET", "your-secret-key-here")
HCAPTCHA_DEFAULT_CONFIG = {"theme": "light", "size": "normal"}

# Misc
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# stdout fix
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

LOGS_DIR = BASE_DIR / "logs"
os.makedirs(LOGS_DIR, exist_ok=True)
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
REVIEWS_LOG_ENABLED = os.getenv("REVIEWS_LOG_ENABLED", "false").lower() == "true"
REVIEWS_LOG_PATH = os.getenv("REVIEWS_LOG_PATH", "/var/log/app/reviews.log")

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    "formatters": {
        "verbose": {
            "format": "%(asctime)s %(levelname)s %(name)s %(message)s",
        },
    },

    "handlers": {
        # ← ОБЯЗАТЕЛЬНО держим console, раз он в root/логгерах
        "console": {
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        # Опциональный файловый хендлер (включается переменной окружения)
        **(
            {
                "reviews_file": {
                    "class": "logging.handlers.RotatingFileHandler",
                    "filename": REVIEWS_LOG_PATH,
                    "maxBytes": 5 * 1024 * 1024,
                    "backupCount": 5,
                    "formatter": "verbose",
                    "encoding": "utf-8",
                }
            }
            if REVIEWS_LOG_ENABLED
            else {}
        ),
    },

    # ← root должен ссылаться только на реально существующие хендлеры
    "root": {
        "handlers": ["console"],
        "level": LOG_LEVEL,
    },

    "loggers": {
        # Логи Django HTTP сервера в консоль
        "django.server": {
            "handlers": ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
        # Твой сервис: либо в файл, либо в консоль
        "services.multi_reviews_service": {
            "handlers": ["reviews_file"] if REVIEWS_LOG_ENABLED else ["console"],
            "level": LOG_LEVEL,
            "propagate": False,
        },
    },
}

# API ключи для отзывов
TRIPADVISOR_API_KEY = os.getenv("TRIPADVISOR_API_KEY", "")
TRIPADVISOR_LOCATION_ID = os.getenv(
    "TRIPADVISOR_LOCATION_ID", "24938712"
)  # БЕЗ префикса 'd'
GOOGLE_PLACES_API_KEY = os.getenv("GOOGLE_PLACES_API_KEY", "")
GOOGLE_PLACE_ID = os.getenv("GOOGLE_PLACE_ID", "")
REVIEWS_CACHE_TIMEOUT = int(os.getenv("REVIEWS_CACHE_TIMEOUT", 86400))

# Parler
PARLER_LANGUAGES = {
    None: (
        {"code": "en"},
    ),
    "default": {"fallbacks": ["en"], "hide_untranslated": False},
}

# ===================== DJANGO TINYMCE =====================

# Базовые настройки TinyMCE
# TINYMCE_API_KEY = 'f80axcxfwy4juoux11elmrxusxzpkbrz85w43nyvug2yta1a'
# TINYMCE_JS_URL = f"https://cdn.tiny.cloud/1/{TINYMCE_API_KEY}/tinymce/6/tinymce.min.js"
TINYMCE_JS_URL = "/static/tinymce/tinymce.min.js"
TINYMCE_COMPRESSOR = False
TINYMCE_SPELLCHECKER = False

# Основная конфигурация (аналог CKEditor 5 'default')
TINYMCE_DEFAULT_CONFIG = {
    "height": 500,
    "width": "auto",
    "menubar": "file edit view insert format tools table",
    "plugins": """
        advlist autolink lists link image charmap preview anchor searchreplace 
        visualblocks code fullscreen insertdatetime media table paste code 
        help wordcount imagetools table lists emoticons codesample nonbreaking pagebreak
    """,
    "toolbar": """
        undo redo | styles | bold italic underline strikethrough | 
        forecolor backcolor | alignleft aligncenter alignright alignjustify |
        bullist numlist outdent indent | link image media swipergallery | 
        table | removeformat code fullscreen help
    """,
    "external_plugins": {
        "swipergallery": "/static/tinymce/plugins/swipergallery/plugin.js"
    },
    # Стили для заголовков (аналог heading в CKEditor)
    "style_formats": [
        {"title": "Paragraph", "format": "p", "classes": "mt-20"},
        {"title": "Heading 1", "format": "h1"},
        {"title": "Heading 2", "format": "h2", "classes": "text-30 md:text-24"},
        {"title": "Heading 3", "format": "h3"},
        {"title": "Heading 4", "format": "h4"},
        {"title": "Heading 5", "format": "h5"},
        {"title": "Heading 6", "format": "h6"},
        {
            "title": "CTA Button",
            "selector": "a",
            "classes": "cta-button button -md -dark-1 bg-accent-1 text-white",
        },
        {
            "title": "CTA Outline",
            "selector": "a",
            "classes": "cta-button-outline button -outline-accent-1 text-accent-1",
        },
    ],
    # Цвета (аналог fontColor в CKEditor)
    "color_map": [
        "000000",
        "Black",
        "4D4D4D",
        "Dark grey",
        "999999",
        "Grey",
        "E6E6E6",
        "Light grey",
        "FFFFFF",
        "White",
        "E64C4C",
        "Red",
        "E6804C",
        "Orange",
        "E6E64C",
        "Yellow",
        "99E64C",
        "Light green",
        "4CE64C",
        "Green",
        "4CE699",
        "Aquamarine",
        "4CE6E6",
        "Turquoise",
        "4C99E6",
        "Light blue",
        "4C4CE6",
        "Blue",
        "994CE6",
        "Purple",
        "E64CE6",
        "Magenta",
        "E64C99",
        "Pink",
    ],
    # Настройки изображений (аналог image в CKEditor)
    "image_advtab": True,
    "image_caption": True,
    "image_title": True,
    "automatic_uploads": True,
    "file_picker_types": "image",
    "images_upload_url": "/tinymce/upload/",
    "images_reuse_filename": False,
    # Таблицы (аналог table в CKEditor)
    "table_toolbar": "tableprops tabledelete | tableinsertrowbefore tableinsertrowafter tabledeleterow | tableinsertcolbefore tableinsertcolafter tabledeletecol",
    "table_appearance_options": True,
    "table_grid": True,
    "table_resize_bars": True,
    "table_default_attributes": {"border": "1"},
    "table_default_styles": {"border-collapse": "collapse", "width": "100%"},
    # Контент CSS (стили как в CKEditor)
    "content_css": "/static/css/ckeditor-content.css",
    "content_style": """
        body { 
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 16px;
            line-height: 1.6;
            color: #32373c;
            padding: 20px;
        }
    """,
    # Разрешенные элементы (аналог htmlSupport в CKEditor)
    "extended_valid_elements": """
        div[class|style|data-*],
        span[class|style|data-*],
        img[class|src|alt|title|width|height|loading|data-*],
        a[href|target|rel|class|style],
        iframe[src|width|height|frameborder|allow|allowfullscreen|title|loading|referrerpolicy],
        figure[class|data-*],
        table[class|style|border|cellpadding|cellspacing],
        td[class|style|colspan|rowspan|data-label],
        th[class|style|colspan|rowspan|data-label]
    """,
    "valid_classes": {
        "div": "table-responsive,table-stack,stack-item,image-gallery,gallery-grid,gallery-item,media",
        "img": "gallery-image",
        "table": "compact,striped,lake-como-table,table-normal",
        "span": "stack-label,stack-value,stack-header",
        "h2": "text-30,md:text-24",
        "p": "mt-20",
        "ul": "list-disc,mt-20",
        "ol": "numbered-list,mt-20",
    },
    # Опции
    "branding": False,
    "promotion": False,
    "relative_urls": False,
    "remove_script_host": False,
    "convert_urls": True,
    "cleanup": True,
    "cleanup_on_startup": True,
    "paste_as_text": False,
    "paste_data_images": True,
    "browser_spellcheck": True,
    "contextmenu": "link image table",
}

# Конфигурация для блога
TINYMCE_BLOG_CONFIG = {
    "height": 600,
    "width": "auto",
    "menubar": "file edit view insert format tools table",
    "plugins": """
        advlist autolink lists link image charmap preview anchor searchreplace 
        visualblocks code fullscreen insertdatetime media table paste code 
        help wordcount imagetools table lists emoticons codesample nonbreaking pagebreak
    """,
    "toolbar": """
        undo redo | styles | bold italic underline strikethrough | 
        forecolor backcolor | alignleft aligncenter alignright alignjustify |
        bullist numlist outdent indent | link image media swipergallery | 
        table | removeformat code fullscreen help
    """,
    "external_plugins": {
        "swipergallery": "/static/tinymce/plugins/swipergallery/plugin.js"
    },
    # Стили для блога
    "style_formats": [
        {"title": "Paragraph", "format": "p", "classes": "mt-20"},
        {"title": "Heading 1", "format": "h1"},
        {"title": "Heading 2", "format": "h2", "classes": "text-30 md:text-24"},
        {"title": "Heading 3", "format": "h3"},
        {"title": "Heading 4", "format": "h4"},
        {"title": "Heading 5", "format": "h5"},
        {"title": "Heading 6", "format": "h6"},
        {
            "title": "Numbered List (mt-20)",
            "selector": "ol",
            "classes": "numbered-list mt-20",
        },
        {
            "title": "CTA Button",
            "selector": "a",
            "classes": "cta-button button -md -dark-1 bg-accent-1 text-white",
        },
        {
            "title": "CTA Outline",
            "selector": "a",
            "classes": "cta-button-outline button -outline-accent-1 text-accent-1",
        },
    ],
    # Специальные ссылки для блога (аналог link decorators в CKEditor)
    "link_class_list": [
        {"title": "Normal Link", "value": ""},
        {
            "title": "CTA Button",
            "value": "cta-button button -md -dark-1 bg-accent-1 text-white",
        },
        {
            "title": "CTA Button Outline",
            "value": "cta-button-outline button -outline-accent-1 text-accent-1",
        },
        {
            "title": "WhatsApp Button",
            "value": "whatsapp-button button -md bg-success-1 text-white",
        },
    ],
    "link_default_target": "_self",
    "target_list": [
        {"title": "Same window", "value": "_self"},
        {"title": "New window", "value": "_blank"},
    ],
    # Цвета для блога
    "color_map": [
        "000000",
        "Black",
        "4D4D4D",
        "Dark grey",
        "999999",
        "Grey",
        "E6E6E6",
        "Light grey",
        "FFFFFF",
        "White",
        "E64C4C",
        "Red",
        "E6804C",
        "Orange",
        "E6E64C",
        "Yellow",
        "99E64C",
        "Light green",
        "4CE64C",
        "Green",
        "4CE699",
        "Aquamarine",
        "4CE6E6",
        "Turquoise",
        "4C99E6",
        "Light blue",
        "4C4CE6",
        "Blue",
        "994CE6",
        "Purple",
        "E64CE6",
        "Magenta",
        "E64C99",
        "Pink",
    ],
    # Изображения
    "image_advtab": True,
    "image_caption": True,
    "automatic_uploads": True,
    "images_upload_url": "/tinymce/upload/",
    "file_picker_types": "image",
    # Таблицы с расширенными настройками
    "table_toolbar": "tableprops tabledelete | tableinsertrowbefore tableinsertrowafter tabledeleterow | tableinsertcolbefore tableinsertcolafter tabledeletecol | tablecellprops",
    "table_appearance_options": True,
    "table_advtab": True,
    "table_cell_advtab": True,
    "table_row_advtab": True,
    "table_class_list": [
        {"title": "Default", "value": ""},
        {"title": "Compact", "value": "compact"},
        {"title": "Striped", "value": "striped"},
        {"title": "Lake Como Table", "value": "lake-como-table"},
    ],
    # Медиа (аналог mediaEmbed в CKEditor)
    "media_live_embeds": True,
    "media_dimensions": True,
    "media_poster": True,
    # Контент CSS
    "content_css": "/static/css/ckeditor-content.css",
    "content_style": """
        /* WordPress-подобные стили */
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 16px;
            line-height: 1.6;
            color: #32373c;
            background: #fff;
            padding: 20px 24px;
        }
        p { margin: 0 0 1em 0; }
        p.mt-20 { margin-top: 20px; }
        h1, h2, h3, h4, h5, h6 {
            color: #23282d;
            font-weight: 600;
            margin: 1.5em 0 0.5em 0;
            line-height: 1.3;
        }
        h1 { font-size: 2.2em; margin-top: 1em; }
        h2 { font-size: 1.8em; }
        h2.text-30 { font-size: 1.875em; }
        h3 { font-size: 1.5em; }
        h4 { font-size: 1.25em; }
        h5 { font-size: 1.1em; }
        h6 { font-size: 1em; font-weight: 700; }
        a { color: #0073aa; text-decoration: none; }
        a:hover { color: #005177; text-decoration: underline; }
        blockquote {
            border-left: 4px solid #0073aa;
            margin: 1.5em 0;
            padding: 0 0 0 1em;
            font-style: italic;
            color: #666;
        }
        img {
            max-width: 100%;
            height: auto;
            border-radius: 4px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
            margin: 1em 0;
        }
        table {
            border-collapse: collapse;
            width: 100%;
            margin: 1em 0;
        }
        table td, table th {
            border: 1px solid #e1e1e1;
            padding: 8px 12px;
            text-align: left;
        }
        table th {
            background: #f9f9f9;
            font-weight: 600;
            color: #23282d;
        }
        code {
            background: #f1f1f1;
            color: #d63384;
            padding: 2px 4px;
            border-radius: 3px;
            font-family: Monaco, Consolas, monospace;
            font-size: 0.9em;
        }
        ul, ol { margin: 1em 0; padding-left: 2em; }
        li { margin: 0.5em 0; }
        .cta-button, .cta-button-outline, .whatsapp-button {
            display: inline-block;
            padding: 12px 30px;
            margin: 10px auto;
            text-align: center;
        }
    """,
    # Разрешенные элементы
    "extended_valid_elements": """
        iframe[src|width|height|frameborder|allow|allowfullscreen|title|loading|referrerpolicy],
        div[class|style|data-*],
        span[class|style|data-*],
        a[href|target|rel|class|style],
        figure[class|data-*],
        img[class|src|alt|loading|data-*],
        table[class|style],
        td[data-label|class],
        th[data-label|class],
        h2[class],
        p[class],
        ol[class],
        ul[class]
    """,
    "valid_classes": {
        "h2": "text-30,md:text-24",
        "p": "mt-20",
        "ol": "numbered-list,mt-20",
        "a": "cta-button,cta-button-outline,whatsapp-button,button,-md,-dark-1,bg-accent-1,text-white,-outline-accent-1,text-accent-1,bg-success-1",
        "div": "table-responsive,image-gallery,media",
        "figure": "media",
    },
    # Опции
    "branding": False,
    "promotion": False,
    "relative_urls": False,
    "convert_urls": True,
    "paste_as_text": False,
    "contextmenu": "link image table",
}

# Конфигурация для туров
TINYMCE_TOUR_CONFIG = {
    "height": 600,
    "width": "auto",
    "menubar": "file edit view insert format tools table",
    "plugins": """
        advlist autolink lists link image charmap preview anchor searchreplace 
        visualblocks code fullscreen insertdatetime media table paste code 
        help wordcount imagetools table lists emoticons codesample nonbreaking pagebreak
    """,
    "toolbar": """
        undo redo | styles | bold italic underline strikethrough | 
        forecolor backcolor | alignleft aligncenter alignright alignjustify |
        bullist numlist outdent indent | link image media swipergallery | 
        table | removeformat code fullscreen help
    """,
    "external_plugins": {
        "swipergallery": "/static/tinymce/plugins/swipergallery/plugin.js"
    },
    # Стили для туров (упрощенные)
    "style_formats": [
        {"title": "Paragraph", "format": "p", "classes": "mt-20"},
        {"title": "Heading 1", "format": "h1"},
        {"title": "Heading 2", "format": "h2", "classes": "text-30 md:text-24"},
        {"title": "Heading 3", "format": "h3"},
        {"title": "Heading 4", "format": "h4"},
        {
            "title": "Numbered List (mt-20)",
            "selector": "ol",
            "classes": "numbered-list mt-20",
        },
        {
            "title": "CTA Button",
            "selector": "a",
            "classes": "cta-button button -md -dark-1 bg-accent-1 text-white",
        },
        {
            "title": "CTA Outline",
            "selector": "a",
            "classes": "cta-button-outline button -outline-accent-1 text-accent-1",
        },
    ],
    # Изображения
    "image_advtab": True,
    "automatic_uploads": True,
    "images_upload_url": "/tinymce/upload/",
    "file_picker_types": "image",
    # Таблицы
    "table_toolbar": "tableprops tabledelete | tableinsertrowbefore tableinsertrowafter tabledeleterow | tableinsertcolbefore tableinsertcolafter tabledeletecol",
    "table_appearance_options": True,
    # Медиа
    "media_live_embeds": True,
    # Контент CSS (те же стили что и для блога)
    "content_css": "/static/css/ckeditor-content.css",
    "content_style": """
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            font-size: 16px;
            line-height: 1.6;
            color: #32373c;
            padding: 20px;
        }
        p.mt-20 { margin-top: 20px; }
        h2.text-30 { font-size: 1.875em; }
        ol.numbered-list { margin-top: 20px; }
    """,
    # Разрешенные элементы
    "extended_valid_elements": """
        iframe[src|width|height|frameborder|allow|allowfullscreen|title|loading|referrerpolicy],
        div[class|data-*],
        figure[class|data-*],
        h2[class],
        p[class],
        ol[class]
    """,
    "valid_classes": {
        "h2": "text-30,md:text-24",
        "p": "mt-20",
        "ol": "numbered-list,mt-20",
        "figure": "media",
    },
    # Опции
    "branding": False,
    "promotion": False,
    "relative_urls": False,
    "convert_urls": True,
}

# Настройки загрузки файлов (аналог CKEDITOR_5_UPLOAD_PATH)
TINYMCE_UPLOAD_PATH = "blog/content/"
TINYMCE_IMAGE_UPLOAD_ENABLED = True
TINYMCE_FILE_UPLOAD_ENABLED = True
TINYMCE_ALLOWED_FILE_TYPES = ["jpeg", "jpg", "png", "gif", "webp", "pdf", "doc", "docx"]


# Теги / изображения / пагинация
TAGGIT_CASE_INSENSITIVE = True

THUMBNAIL_FORMAT = "WEBP"
THUMBNAIL_QUALITY = 85
THUMBNAIL_PRESERVE_FORMAT = False

PAGINATE_BY = 10

FILE_UPLOAD_MAX_MEMORY_SIZE = 10 * 1024 * 1024  # 10MB
DATA_UPLOAD_MAX_MEMORY_SIZE = 15 * 1024 * 1024  # 15MB

ALLOWED_IMAGE_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif", ".webp"]
MAX_IMAGE_SIZE = 5 * 1024 * 1024  # 5MB

IMAGE_QUALITY = 85
MAX_IMAGE_WIDTH = 1200
MAX_IMAGE_HEIGHT = 1200

THUMBNAIL_ALIASES = {
    "": {
        # Hero и слайдеры главной
        "hero_mobile": {"size": (640, 360), "crop": "smart", "quality": 80, "format": "WEBP"},
        "hero_tablet": {"size": (1024, 576), "crop": "smart", "quality": 85, "format": "WEBP"},
        "hero_desktop": {"size": (1920, 1080), "crop": "smart", "quality": 90, "format": "WEBP"},
        
        # Карточки туров
        "tour_card_mobile": {"size": (400, 280), "crop": "smart", "quality": 80, "format": "WEBP"},
        "tour_card_tablet": {"size": (600, 420), "crop": "smart", "quality": 85, "format": "WEBP"},
        "tour_card_desktop": {"size": (800, 560), "crop": "smart", "quality": 90, "format": "WEBP"},
        
        # Детальная страница тура (галерея)
        "tour_gallery_mobile": {"size": (480, 320), "crop": "smart", "quality": 80, "format": "WEBP"},
        "tour_gallery_tablet": {"size": (768, 512), "crop": "smart", "quality": 85, "format": "WEBP"},
        "tour_gallery_desktop": {"size": (1200, 800), "crop": "smart", "quality": 90, "format": "WEBP"},
        
        # Блог - карточки
        "blog_card_mobile": {"size": (400, 300), "crop": "smart", "quality": 80, "format": "WEBP"},
        "blog_card_tablet": {"size": (600, 450), "crop": "smart", "quality": 85, "format": "WEBP"},
        "blog_card_desktop": {"size": (800, 600), "crop": "smart", "quality": 90, "format": "WEBP"},
        
        # Блог - детальная страница
        "blog_hero_mobile": {"size": (640, 400), "crop": "smart", "quality": 80, "format": "WEBP"},
        "blog_hero_tablet": {"size": (1024, 640), "crop": "smart", "quality": 85, "format": "WEBP"},
        "blog_hero_desktop": {"size": (1920, 1200), "crop": "smart", "quality": 90, "format": "WEBP"},
        
        # Команда (About page)
        "team_mobile": {"size": (480, 480), "crop": "smart", "quality": 80, "format": "WEBP"},
        "team_tablet": {"size": (768, 768), "crop": "smart", "quality": 85, "format": "WEBP"},
        "team_desktop": {"size": (1024, 1024), "crop": "smart", "quality": 90, "format": "WEBP"},
        
        # Отзывы (Reviews)
        "review_thumb": {"size": (60, 60), "crop": "smart", "quality": 85, "format": "WEBP"},
        "review_avatar": {"size": (100, 100), "crop": "smart", "quality": 85, "format": "WEBP"},
        
        # Миниатюры для виджетов
        "widget_thumb": {"size": (80, 80), "crop": "smart", "quality": 80, "format": "WEBP"},
        
        # OG Image для соцсетей
        "og_image": {"size": (1200, 630), "crop": "smart", "quality": 90, "format": "JPEG"},
    }
}
