from django import template
register = template.Library()



@register.filter
def upper_goods(obj):
    return obj.upper()