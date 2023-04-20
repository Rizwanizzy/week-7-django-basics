from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.
def register(request):
    if 'username' in request.session:
        return redirect('/')
    if 'admin' in request.session:
        return redirect('admin_home')
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'username is taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email is taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email,
                                                first_name=first_name,
                                                last_name=last_name)
                user.save()
                messages.info(request, 'user created')
                return redirect('login')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')

    else:
        return render(request, 'register.html')


def login(request):
    if 'username' in request.session:
        return redirect('/')
    if 'admin' in request.session:
        return redirect('admin_home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and not user.is_superuser:
            request.session['username']=username
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    if 'username' in request.session or 'admin' in request.session:
        request.session.flush()
    auth.logout(request)
    return redirect('login')
