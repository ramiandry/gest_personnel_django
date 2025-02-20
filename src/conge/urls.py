from django.urls import path
from .views import conges

urlpatterns = [
    path("conges/", conges, name="conges" ),
]