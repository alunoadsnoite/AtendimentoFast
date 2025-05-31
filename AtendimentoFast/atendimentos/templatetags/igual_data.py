from django import template

register = template.Library()

@register.filter
def igual_data(data1, data2):
    return data1 == data2
