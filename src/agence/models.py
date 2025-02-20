from django.db import models

# Create your models here.
#creat° table nom_class=nom_tale
class Agence(models.Model):
    nom= models.CharField( max_length=120, null=False)
    adresse=models.CharField( max_length=120, null=False)
    email=models.CharField( max_length=120)
    tel=models.CharField(max_length=15)