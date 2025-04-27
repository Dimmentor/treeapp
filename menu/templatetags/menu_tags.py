from django import template
from menu.models import Menu

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = Menu.objects.filter(parent=None)
    return {'menu_items': menu_items, 'menu_name': menu_name}