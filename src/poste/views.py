from django.shortcuts import redirect, render
from employee.models import Employees
from poste.models import Postes
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def poste(request):
    data=Postes.objects.all()
    dataPersonnel=Employees.objects.all()
    for datas in data:
        print(datas.pk,datas.nom_poste, datas.photo.url)
    if request.POST.get("btnAction")=='btnAjouter':
        postes=request.POST.get("poste")
        images=request.FILES['image']
        print(postes, images)
        Postes.objects.create(nom_poste=postes, photo=images)
        print(Postes.objects.last())
        return redirect('postes')
    elif request.POST.get("btnAction")=="modPoste":
        id=request.POST.get("id")
        postes=Postes.objects.get(pk=id)
        postes.nom_poste=request.POST.get("poste")
        postes.save()
        return redirect('postes')
    elif request.POST.get("btnAction")=="modProfil":
        id=request.POST.get("id")
        postes=Postes.objects.get(pk=id)
        postes.photo=request.FILES['image']
        postes.save()
        return redirect('postes')


    return render(request, "postes/index.html", {"data":data, "dataPersonnel":dataPersonnel})