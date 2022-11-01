from django import template


register = template.Library()


@register.filter
def template_float_to_int(_float):
    return int(_float)
