import html
import re

from django import template
from django.utils.html import strip_tags

register = template.Library()


@register.filter
def clean_html_excerpt(value):
    if value is None:
        return ''
    text = html.unescape(str(value))
    text = strip_tags(text)
    text = re.sub(r'<[^>]*>', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text
