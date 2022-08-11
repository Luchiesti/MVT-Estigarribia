import ast

from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter(name='lookup')
def lookup(value, arg):
    return value[arg]
