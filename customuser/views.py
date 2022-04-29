from django.shortcuts import render, redirect
from django.http import HttpResponse
# Authentication Libraries
from django.contrib.auth import authenticate, login, logout
from .models import User

# Create your views here.
def home(request):
    return render(request, 'home.html')

def signin(request):

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

    user = authenticate(email = email, password = password)

    if user is not None:
        login(request, user)
        return render(request, 'signin.html')
    else:
        return HttpResponse("<h2>Wrong Credintials buddy</h2>")

    return HttpResponse("<h2>Nah</h2>")

def signout(request):

    logout(request)

    return redirect('home')