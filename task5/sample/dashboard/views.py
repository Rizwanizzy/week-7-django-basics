from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import authenticate ,login
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def admin_home(request):
    if 'admin' in request.session:
        all_users=User.objects.order_by('id')
        return render(request,'admin_home.html',{'all_users':all_users})
    else:
        return redirect('admin_login')

def admin_login(request):
    if 'username' in request.session:
        return redirect('/')
    if 'admin' in request.session:
        return redirect('admin_home')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user.is_superuser:
            login(request, user)
            request.session['admin']=username
            return redirect('admin_home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('admin_login')
    else:
        return render(request, 'admin_login.html')
    
def add_user(request):
    if 'username' in request.session:
        return redirect('/')
    if 'admin' in request.session:
        if request.method == 'POST':
            username = request.POST['username']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'username is taken')
                    return redirect('add_user')
                else:
                    user = User.objects.create_user(username=username, password=password1)
                    user.save()
                    messages.info(request, 'user created')
                    return redirect('admin_home')
            else:
                messages.info(request, 'password not matching')
                return redirect('add_user')

        else:
            return render(request,'add_user.html')
    
def update_user(request,id):
    if 'username' in request.session:
        return redirect('/')
    if 'admin' in request.session:
        user=User.objects.get(id=id)
        if request.method=='POST':
            username=request.POST['username']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            email=request.POST['email']
            user=User(id=id,username=username,first_name=first_name,last_name=last_name,email=email)
            user.save()
            return redirect('admin_home')
        else:
            return render(request,'update_user.html',{'user':user})
    
def delete_user(request,id):
    if 'username' in request.session:
        return redirect('/')
    if 'admin' in request.session:
        user=User.objects.get(id=id)
        if request.method=='POST':
            user.delete()
            return redirect('admin_home')
        else:
            return render(request,'delete_user.html',{'user':user})
    
def search(request):
    if 'username' in request.session:
        return redirect('/')
    if 'admin' in request.session:
        if request.method=='GET':
            query=request.GET['query']
            all_users=User.objects.filter(Q(username__contains=query) |Q(first_name__contains=query) | Q(last_name__contains=query) | Q(email__contains=query) )
            return render(request,'search.html',{'all_users':all_users})
        else:
            return redirect('admin_home')