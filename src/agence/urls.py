from django.urls import path
from .views import agence

urlpatterns = [
    path("agence/", agence, name="agence" ),
]