from django.urls import path, include
from . import views

urlpatterns = [
    path("hello", views.home),
    path("hotels", views.gethotels),
    path("classhotels", views.HotelsList.as_view())
]