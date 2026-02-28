from django.urls import path
from . import views # Импортируем представления из текущего приложения

# Этот список urlpatterns будет подключен к главному urls.py проекта
urlpatterns = [ # Маршрут для корня приложения
    path('details/', views.hello, name='myapp_details'),
]