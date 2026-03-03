from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_me, name='about_me'),           # /about/
    path('contacts/', views.my_contacts, name='contacts'),  # /about/contacts/
]