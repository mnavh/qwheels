from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
# Create your views here.

list_topbar = [{"title":'Home',"link":'main_page_html'},{"title":'Vendors',"link":'index'},{"title":'Deals',"link":'deals'},{"title":'Track Order',"link":'track-order'},{"title":'Blog',"link":'index'},{"title":'Contact Us',"link":''},{"title":'About Us',"link":'about_us'}]
context = {
        'menu':list_topbar
    }
def main_page(request):
    print("Rendering main page...")
    request.session['session_id']=request.user.id
    print(request.user.username)
    print(request.session)
    print(request.session.session_key)
    print(request.user)
    if request.user.is_authenticated:
        print("Authenticated User")
        username_text=request.user.username
        return render(request, 'Qwheel_App/index.html', {'menu':list_topbar, 'username':username_text})
    
    else:
        print("Not Logged in")
        username_text='Login'
        return render(request, 'Qwheel_App/index.html', {'menu':list_topbar, 'username':username_text})
    

    # return render(request, 'Qwheel_App/index.html', {'menu':list_topbar, 'username':username_text})

def about_us_page(request):
    return render(request, 'Qwheel_App/about-us.html', context)

def deals_page(request):
    print("Rendering deals")
    return render(request, 'Qwheel_App/deals.html', context)

def account_page(request):
    if request.method=='GET':
        
        print("Its a Get Requst...")
        # print(reque)
        return render(request, 'Qwheel_App/account.html', {'form':UserCreationForm, 'form1':AuthenticationForm, 'menu':list_topbar})
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
                login(request, user)
                return redirect(main_page)
                
                # return render(request, 'Qwheel_App/index.html', {'menu':list_topbar, 'username':username_text})
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




