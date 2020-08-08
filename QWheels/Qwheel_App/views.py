from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from .forms import add_vendor, add_product
from django.contrib import messages
import pdb

# Create your views here.

list_topbar = [{"title":'Home',"link":'main_page_html'},{"title":'Vendors',"link":'index'},{"title":'Deals',"link":'deals'},{"title":'Track Order',"link":'track-order'},{"title":'Blog',"link":'index'},{"title":'Contact Us',"link":''},{"title":'About Us',"link":'about_us'}]
context = {
        'menu':list_topbar
    }
def main_page(request):
    print("Rendering main page...")
    return render(request, 'Qwheel_App/index.html', context)

def about_us_page(request):
    return render(request, 'Qwheel_App/about-us.html', context)

def deals_page(request):
    print("Rendering deals")
    return render(request, 'Qwheel_App/deals.html', context)

def account_page(request):
    if request.method=='GET':
        print("Its a Get Requst...")
        return render(request, 'Qwheel_App/account.html', {'form':UserCreationForm, 'form1':AuthenticationForm})
    elif request.method=='POST':
        print("its a post a request")
        print(request.POST.get('submit'))
        if request.POST.get('submit')=='login':
            print(request.POST)
            username=request.POST['username']
            password=request.POST['password']
            user=authenticate(username=username,password=password)
            print("Authentication Result : ",user)
            if user is not None:
                return render(request, 'Qwheel_App/index.html', {})
            else:
                return render(request, 'Qwheel_App/account.html', {'form':UserCreationForm, 'form1':AuthenticationForm})

        if request.POST.get('submit')=='register':
            print(request.POST)
            print(request.POST['password1'])  #Get User password from html form field
            print(request.POST.get('username'))
            if request.POST['password1']==request.POST['password2']:
                User.objects.create_user(request.POST['username'],'NA',request.POST['password1'])
            else:
                print("Password 2 didnt matched...")

            return render(request, 'Qwheel_App/account.html', {'form':UserCreationForm, 'form1':AuthenticationForm})

        # if request.POST['login_btn']:
        #     return render(request, 'index.html', {})
        # else:
        #     pass

def addvendor(request):
    if request.method == 'POST':
        form = add_vendor(request.POST or None, request.FILES or None)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            print("saved vendor!")
        else:
            messages.error(request, "Error")
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = add_vendor()
        # pdb.set_trace()

    return render(request, 'Qwheel_App/add-vendor.html', {'form': form})


def addproduct(request):
    if request.method == 'POST':
        form = add_product(request.POST or None, request.FILES or None)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            print("saved product!")
        else:
            messages.error(request, "Error")
            
    # if a GET (or any other method) we'll create a blank form
    else:
        form = add_product()

    return render(request, 'Qwheel_App/add-product.html', {'form': form})

