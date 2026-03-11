from django.urls import path
from . import views

urlpatterns = [
    path("", views.coworking_page, name="coworking"),
]