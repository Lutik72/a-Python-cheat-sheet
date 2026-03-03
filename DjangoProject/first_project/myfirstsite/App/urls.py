from django.urls import path
from . import views # импортировать модуль views.py нужно из нашего приложения, заменив точку

urlpatterns = [
 path('about/', views.about_page, name='about')
]