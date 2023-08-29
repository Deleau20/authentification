from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages

# Create your views here.


def home(request):
    return render(request, 'verification/index.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
    
        utilisateur = User.objects.create_user(username, email, password)
        utilisateur.first_name = firstname
        utilisateur.last_name = lastname
        utilisateur.save()
        messages.success(request, "Votre compte a été créé avec succès !")
        return redirect('login')
    return render(request, 'verification/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate (request, username=username, password=password)
        if user is not None:
            auth_login(request, user)
            first_name = request.user.first_name
            return render(request, 'verification/index.html', { 'first_name': first_name })
        else:
            messages.error(request, "Identifiants invalides.")
            return redirect('login')
    return render(request, 'verification/login.html')

def logOut(request):
    logout(request)
    messages.success(request, "Vous avez été déconnecté avec succès !")
    return redirect('home')