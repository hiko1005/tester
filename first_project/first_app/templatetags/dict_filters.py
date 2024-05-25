from django import template
register = template.Library()
@register.filter
def get_val(dictionary, key):
    if type(dictionary) == type(dict()):
        return dictionary.get(key)
    else:
        return getattr(dictionary, key)