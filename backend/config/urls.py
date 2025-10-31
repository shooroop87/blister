# backend/config/urls.py - ИСПРАВЛЕННАЯ ВЕРСИЯ С ГИБКИМИ URL

import os

# Импорты из core приложения
from core.sitemaps import CompleteSitemap
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.http import HttpResponse
from django.urls import include, path, re_path
from django.views.decorators.http import require_GET
from django.views.i18n import set_language


# --- URLs без языкового префикса ---
urlpatterns = [
    path("set-language/", set_language, name="set_language"),
    # Django admin
    path("admin/", admin.site.urls),
    path("", include("core.health")),  # даёт /health/
    path("tinymce/", include("tinymce.urls")),  # ЭТО ОБЯЗАТЕЛЬНО!
    # Django-Filer маршруты
    path("filer/", include("filer.urls")),
]


# --- Языковые маршруты ---
urlpatterns += i18n_patterns(
    path("", include("core.urls")),
    prefix_default_language=False,
)

# === МЕДИА ФАЙЛЫ ===
# Проверяем и создаем медиа-директорию если не существует
if not os.path.exists(settings.MEDIA_ROOT):
    os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
    print(f"✅ Создана медиа-директория: {settings.MEDIA_ROOT}")

if settings.DEBUG:
    print("🐛 DEBUG=True: Настройка обслуживания медиа через Django...")
    from django.conf.urls.static import static

    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    if "django_browser_reload" in settings.INSTALLED_APPS:
        urlpatterns += [
            path("__reload__/", include("django_browser_reload.urls")),
        ]
else:
    print("🚀 PRODUCTION MODE: Настройка обслуживания медиа для production...")
    from django.views.static import serve

    urlpatterns += [
        re_path(
            r"^media/(?P<path>.*)$",
            serve,
            {"document_root": settings.MEDIA_ROOT},
        ),
    ]

print(f"🔧 Итого URL patterns: {len(urlpatterns)}")
print(f"🔧 DEBUG: {settings.DEBUG}")
print(f"🔧 MEDIA_URL: {settings.MEDIA_URL}")

