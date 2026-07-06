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


@register.filter
def range_filter(value):
    """Create a range from 0 to value-1"""
    try:
        return range(int(value))
    except (ValueError, TypeError):
        return range(0)


@register.filter
def range_from(value, start):
    """Create a range from start to value-1"""
    try:
        return range(int(start), int(value))
    except (ValueError, TypeError):
        return range(0)
