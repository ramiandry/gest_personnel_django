from django.db import models
from poste.models import Postes
from agence.models import Agence

# Create your models here.


class Employees(models.Model):
    poste=models.ForeignKey(Postes,on_delete=models.SET_NULL, null=True)
    agence=models.ForeignKey(Agence,on_delete=models.SET_NULL, null=True)
    nom=models.CharField(max_length=120, blank=False)
    prenom=models.CharField(max_length=120)
    sexe=models.BooleanField(null=True)
    date_de_naissance=models.DateField()
    date_embauche=models.DateField()
    avatar=models.ImageField(upload_to="products/", blank=True, null=True)
