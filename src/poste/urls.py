from django.urls import path
from .views import poste

urlpatterns = [
    path("postes/", poste, name="postes" ),
]