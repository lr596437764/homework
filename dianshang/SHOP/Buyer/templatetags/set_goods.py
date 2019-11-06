from django import template
register = template.Library()



@register.filter
def upper_goods(obj):
    return obj.upper()


@register.filter("set_phone")
def set_phone(obj):
    result=obj[:3]+"****"+obj[7:]
    return result