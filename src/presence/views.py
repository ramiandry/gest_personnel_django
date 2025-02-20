from django.shortcuts import render, redirect
from employee.models import Employees
from presence.models import Presence
from django.contrib.auth.decorators import login_required
from datetime import datetime

# Create your views here.
@login_required
def presence(request):
    #data=Presence.objects.filter(dateHeure__month=datetime.now().date().month,dateHeure__day=datetime.now().date().day, dateHeure__year=datetime.now().date().year )
    data=Presence.objects.all()
    #Ajout de nouveau personnel
    if request.POST.get("btnAction")=='addPresence':
        id=request.POST.get("id")
        personnel=Employees.objects.get(pk=id)
        print(datetime.now().time().hour)
        if(datetime.now().time().hour<9):
            Presence.objects.create(etat=1, employee=personnel)
        elif(datetime.now().time().hour>=9):
            Presence.objects.create(etat=2, employee=personnel)
        return redirect("presences")
    return render(request, 'presence/index.html', {"data":data})
