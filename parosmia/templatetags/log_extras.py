from django import template

register = template.Library()

@register.filter
def replace_lbr(value):
    return value.replace("\n","<br/>\n")