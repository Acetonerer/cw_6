from django import template

register = template.Library()


@register.simple_tag
def mediapath(val):
    return f'/media/{val}'
