# templatetags/custom_filters.py
from django import template

register = template.Library()

@register.filter(name='get_attr')
def get_attribute(obj, attr):
    if hasattr(obj,attr):
        return getattr(obj, attr)
    else: return None