from django.shortcuts import render
from menu.models import Menu

def index_view(request):
    menu_items = Menu.objects.filter(parent=None)
    return render(request, 'index.html', {'menu_items': menu_items})