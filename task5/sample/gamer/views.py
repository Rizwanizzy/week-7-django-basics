from django.shortcuts import render,redirect
# from sample import accounts
# from accounts.views import *

# Create your views here.
def index(request):
    if 'username' in request.session:
        return render(request, 'index.html')
    return redirect('login')
