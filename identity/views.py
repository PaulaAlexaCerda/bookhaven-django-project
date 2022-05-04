import re
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate


def login_view(request):
    error_message = ''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
 
        if user:
           login(request, user) 
           return redirect('home')
        error_message = "Username and password doesn't exists"

    return render (request, 'identity/customlogin.html', {"error_message":error_message})
