from django.urls import path, include
from myfirstsite import views

urlpatterns = [
    # Основные маршруты
    path('', views.index_page, name='index'),
    path('about/', views.about_page, name='about'),  # страница /about/
    path('app/', include('LutikApp.urls')),
]