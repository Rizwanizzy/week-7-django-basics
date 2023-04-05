from django.shortcuts import render


def login_view(request):
    return render(request, 'login.html')


def home_view(request):
    return render(request, 'home.html')
