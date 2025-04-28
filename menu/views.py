from django.http import HttpResponseNotFound
from django.shortcuts import render
from menu.models import Menu

def index_view(request):
    menu_items = Menu.objects.filter(parent=None)
    return render(request, 'index.html', {'menu_items': menu_items})

def category_view(request, slug):
    try:
        category = Menu.objects.get(slug=slug)
        return render(request, 'category.html', {'category': category})
    except Menu.DoesNotExist:
        return HttpResponseNotFound("<h1>Страница не найдена</h1>")