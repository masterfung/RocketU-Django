__author__ = '@masterfung'

from django import template

register = template.Library()

@register.filter
def suit(list, suit_type):
    return [item for item in list if item.get_suit_display() == suit_type]