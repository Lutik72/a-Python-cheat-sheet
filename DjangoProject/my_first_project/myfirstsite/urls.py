from django.urls import path, include
from myfirstsite import views

urlpatterns = [
    # Основные маршруты
    path('', views.simple_page, name='index'),
    path('app/', include('LutikApp.urls')),
]