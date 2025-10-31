import re

from django import template
from django.utils.html import strip_tags

register = template.Library()


@register.filter
def is_not_empty_html(value):
    """
    Проверяет, содержит ли HTML-текст что-то кроме пустых тегов, &nbsp;, пробелов и других whitespace символов.
    """
    if not value:
        return False

    # Убираем HTML теги
    text = strip_tags(value)

    # Убираем пробельные символы + неразрывные пробелы (в т.ч. \xa0)
    cleaned = re.sub(r"[\s\u00A0]+", "", text)

    return bool(cleaned)
