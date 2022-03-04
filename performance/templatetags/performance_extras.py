import json
from django import template


register = template.Library()


@register.filter
def template_json_dict_to_text(value):
    return ' '.join(['%s: %s' % (k, v) for k, v in json.loads(value).items()])
