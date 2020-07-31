from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

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
        return render(request, 'account.html', {'form':UserCreationForm, 'form1':AuthenticationForm})
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
                return render(request, 'index.html', {})
            else:
                return render(request, 'account.html', {'form':UserCreationForm, 'form1':AuthenticationForm})

        if request.POST.get('submit')=='register':
            print(request.POST)
            print(request.POST['password1'])  #Get User password from html form field
            print(request.POST.get('username'))
            if request.POST['password1']==request.POST['password2']:
                User.objects.create_user(request.POST['username'],'NA',request.POST['password1'])
            else:
                print("Password 2 didnt matched...")

            return render(request, 'account.html', {'form':UserCreationForm, 'form1':AuthenticationForm})

        # if request.POST['login_btn']:
        #     return render(request, 'index.html', {})
        # else:
        #     pass




