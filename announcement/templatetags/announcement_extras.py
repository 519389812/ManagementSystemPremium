from django import template
from django.utils import timezone


register = template.Library()


@register.filter
def template_announcement_is_active(value):
    if value:
        if value.period_close_datetime >= timezone.now() and value.close_datetime >= timezone.now():
            return True
        else:
            return False
    else:
        return True if value.close_datetime >= timezone.now() else False


@register.filter
def template_content_preview(value):
    return value.content[:20]
