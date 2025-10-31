# backend/core/urls.py - С ПЕРЕАДРЕСОВКОЙ СТАРЫХ URL ТУРОВ
from django.urls import path
from django.views.generic import RedirectView

from . import views

urlpatterns = [
    # Главная страница
    path("", views.index, name="index"),
]
