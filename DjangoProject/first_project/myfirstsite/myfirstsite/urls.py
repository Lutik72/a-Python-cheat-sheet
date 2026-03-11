from django.urls import path, include
from myfirstsite import views

urlpatterns = [
    # Основные маршруты
    path('', views.index_page, name='index'),
    path('about/', include('about.urls')),   # все адреса с /about/... идут в about/urls.py
    path("coworking/", include('coworking.urls')),
]