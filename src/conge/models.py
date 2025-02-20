from django.db import models

from employee.models import Employees

# Create your models here.

class Conges(models.Model):
    employee=models.ForeignKey(Employees, on_delete=models.SET_NULL,null=True)
    date_debut=models.DateField(auto_now=True)
    date_fin=models.DateField()
    enPoste=models.BooleanField(default=False)