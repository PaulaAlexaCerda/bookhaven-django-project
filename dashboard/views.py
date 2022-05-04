from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
    context = {
        "title": "Home",
    }
    return render(request, 'dashboard/home.html', context)

def about(request):
    context = {
        "title": "About"
    }
    return render(request, 'dashboard/about.html', context)

