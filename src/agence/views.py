from django.shortcuts import redirect, render

from agence.models import Agence
from django.contrib.auth.decorators import login_required
# Create your views here.
#Annotation, verficat° de connex
@login_required
def agence(request):
    data=Agence.objects.all()
    if request.POST.get("btnAction")=="ajouter":
        #ajouter à la bd
        Agence.objects.create(nom=request.POST.get('nom')
                                , adresse=request.POST.get('adresse')
                                , email=request.POST.get('email')
                                , tel=request.POST.get('tel'))
        return redirect('agence')
    elif request.POST.get('btnAction')=="btnMod":
        id=request.POST.get('id')
        agences=Agence.objects.get(pk=id)
        agences.nom=request.POST.get('nom')
        agences.adresse=request.POST.get('adresse')
        agences.email=request.POST.get('email')
        agences.tel=request.POST.get('tel')
        agences.save()
        return redirect('agence')
    return render(request, 'agence/index.html', {"data":data})