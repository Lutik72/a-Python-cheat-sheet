from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),  # Эта строка уже должна быть
    path("", views.about_page, name="about"),  # /about/
    path("coworking/", include('coworking.urls')),
]
