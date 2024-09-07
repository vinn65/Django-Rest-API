from django.urls import path
from . import views

urlpatterns = [
    path("", views.api_home),
    path("api/", views.api_home),
]
