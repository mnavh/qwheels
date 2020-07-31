from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

<<<<<<< HEAD
list_topbar = [{"title":'Home',"link":''},{"title":'Vendors',"link":''},{"title":'Deals',"link":'deals'},{"title":'Track Order',"link":'track-order.html'},{"title":'Blog',"link":'index.html'},{"title":'Contact Us',"link":'about-us.html'},{"title":'About Us',"link":'about-us.html'}]

def main_page(request):
    print("Rendering main page...")
    context = {
=======
list_topbar = [{"title":'Home',"link":'main_page_html'},{"title":'Vendors',"link":'index'},{"title":'Deals',"link":'deals'},{"title":'Track Order',"link":'track-order'},{"title":'Blog',"link":'index'},{"title":'Contact Us',"link":''},{"title":'About Us',"link":'about_us'}]
context = {
>>>>>>> a8393c724ad8072d64b4e298f65c7b7cb75431bf
        'menu':list_topbar
    }
def main_page(request):
    print("Rendering main page...")
    return render(request, 'Qwheel_App/index.html', context)

def about_us_page(request):
    return render(request, 'Qwheel_App/about-us.html', context)

def deals_page(request):
<<<<<<< HEAD
    print("Deals page")
    return render(request, 'deals.html', {})
=======
    print("Rendering deals")
    return render(request, 'Qwheel_App/deals.html', context)
>>>>>>> a8393c724ad8072d64b4e298f65c7b7cb75431bf

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




