from django.db import models

# Create your models here.
class Postes(models.Model):
    nom_poste=models.CharField(max_length=120)
    photo=models.ImageField(upload_to="products/", blank=True, null=True)