from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path("admin/", admin.site.urls),  # Эта строка уже должна быть
    path("", views.about_page, name="about"),  # /about/
    # path('contacts/', views.my_contacts, name='contacts'),  # /about/contacts/
]
