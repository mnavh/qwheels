from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

# Create your views here.

list_topbar = [{"title":'Home',"link":''},{"title":'Vendors',"link":'index.html'},{"title":'Deals',"link":'deals.html'},{"title":'Track Order',"link":'track-order.html'},{"title":'Blog',"link":'index.html'},{"title":'Contact Us',"link":'about-us.html'},{"title":'About Us',"link":'about-us.html'}]

def main_page(request):
    print("Rendering main page...")
    context = {
        'menu':list_topbar
    }
    return render(request, 'index.html', context)

def deals_page(request):
    return render(request, 'deals.html', {})

def account_page(request):
    if request.method=='GET':
        print("Its a Get Requst...")
        return render(request, 'account.html', {'form':AuthenticationForm})
    else:
        return render(request, 'index.html', {})




