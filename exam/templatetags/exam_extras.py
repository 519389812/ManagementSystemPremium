import json
from django import template
import random


register = template.Library()


@register.filter
def template_split_text(value):
    return [i for i in random.shuffle(value.split(' ')) if i != '']


@register.filter
def template_load_json_as_dict(value):
    return json.loads(value)
