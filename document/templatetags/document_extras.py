from django import template


register = template.Library()


@register.filter
def template_get_dict_value(dict, key):
    return dict.get(key, "")
