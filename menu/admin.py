from django.contrib import admin
from .models import Menu

class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'parent')
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Menu, MenuItemAdmin)