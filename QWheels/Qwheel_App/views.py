from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.
#modified view filesdad

def main_page(request):
    print("Rendering main page...")
    return render(request, 'index.html', {})

def deals_page(request):
    return render(request, 'deals.html', {})

def account_page(request):
    if request.method=='GET':
        print("Its a Get Requst...")
        return render(request, 'account.html', {'form':AuthenticationForm})
    else:
        return render(request, 'index.html', {})




