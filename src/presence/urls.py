from django.urls import path
from .views import presence

urlpatterns = [
    path("presences/", presence, name="presences" ),
]