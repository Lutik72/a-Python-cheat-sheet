from django.contrib import admin
from django.urls import path
from myfirstsite import views

urlpatterns = [
    # Основные маршруты
    path('', views.simple_page, name='index'),  # Простая страница
]