from django.shortcuts import render
from django.contrib.auth.models import User

def home(request):
    if request.user.is_authenticated():
        username = request.user.username
        context = {
            "username" : username,
        }
    else:
        context = {}

    return render(request, "user/home.html",context)