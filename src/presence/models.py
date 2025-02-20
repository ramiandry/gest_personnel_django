from django.db import models

from employee.models import Employees

# Create your models here.

class Presence(models.Model):
    class Etat(models.IntegerChoices):
        present=1,"Present(e)"
        retard=2,"Retard"
        abscent=3,"Abscent(e)"
    dateHeure=models.DateTimeField(auto_now=True)
    etat=models.PositiveSmallIntegerField(choices=Etat.choices)
    employee=models.ForeignKey(Employees, on_delete=models.SET_NULL,null=True)