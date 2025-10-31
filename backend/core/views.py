# backend/core/views.py - УЛУЧШЕННАЯ ВЕРСИЯ С ОТЛАДКОЙ И ИСПРАВЛЕНИЯМИ
import json
import logging
import os
import uuid

import requests

from django.conf import settings
from django.core.files.storage import default_storage
from django.http import (
    Http404,
    HttpResponseRedirect,
    JsonResponse,
)
from django.shortcuts import render
from django.utils import timezone
from django.utils.translation import activate
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.vary import vary_on_headers

# Настройка логгера для отладки
logger = logging.getLogger("core.views")

# --- SendPulse API ключи ---
SENDPULSE_CLIENT_ID = "your_client_id"
SENDPULSE_CLIENT_SECRET = "your_client_secret"
SENDPULSE_LIST_ID = "your_list_id"


def get_sendpulse_token():
    url = "https://api.sendpulse.com/oauth/access_token"
    data = {
        "grant_type": "client_credentials",
        "client_id": SENDPULSE_CLIENT_ID,
        "client_secret": SENDPULSE_CLIENT_SECRET,
    }
    res = requests.post(url, data=data)
    return res.json().get("access_token")


@cache_page(60 * 15)  # Кеширование на 15 минут
@vary_on_headers("Accept-Language")
def index(request):
    """
    Главная страница с последними статьями блога, отзывами из БД и турами.
    """
    logger.info("🏠 ===== Загрузка главной страницы =====")
    context = {}
    return render(request, "pages/index.html", context)
