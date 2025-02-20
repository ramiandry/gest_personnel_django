from django.db import models

from poste.models import Postes

# Create your models here.

class Missions(models.Model):
    poste=models.ForeignKey(Postes,on_delete=models.SET_NULL, null=True)
    type=models.CharField(max_length=150)