from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
# Create your views here.

def logout_user(request):
    logout(request)
    return redirect('login')

def login_user(request):
    if request.method == 'POST':
        #Connexion
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('employee')
    return render(request, 'login/index.html')
