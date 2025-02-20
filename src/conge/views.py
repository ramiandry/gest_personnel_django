from django.shortcuts import redirect, render

from conge.models import Conges
from employee.models import Employees
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def conges(request):
    data=Employees.objects.all()
    dataConges=Conges.objects.all()
    if request.POST.get("btnAction")=="ajouterConge":
        employee=str(request.POST.get('employee')).split(" ")
        print(employee[0], employee[1])
        employees=Employees.objects.get(nom=employee[0], prenom=employee[1])
        Conges.objects.create(employee=employees, date_debut=request.POST.get('debut'), date_fin=request.POST.get('fin'))
        return redirect('conges')
    elif request.POST.get('btnAction')=="btnModPoste":
        id=request.POST.get('id')
        conges=Conges.objects.get(pk=id)
        conges.enPoste=True
        conges.save()
        return redirect('conges')
    return render(request, 'conges/index.html',{"dataEmployee":data, "dataConges":dataConges})

