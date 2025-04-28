from django.urls import path
from menu import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('category/<slug:slug>/', views.category_view, name='category'),
]