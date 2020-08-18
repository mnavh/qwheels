from django.shortcuts import render, redirect
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import get_user_model
User = get_user_model()
from django.contrib.auth import login, authenticate
from .forms import add_vendor, add_product, add_product_img, UserCreationForm
from .models import product_img
from django.forms import modelformset_factory
from django.contrib import messages
import pdb

from django.contrib.auth import login, authenticate, logout
# Create your views here.

list_topbar = [{"title":'Home',"link":'main_page_html'},{"title":'Vendors',"link":'index'},{"title":'Deals',"link":'deals'},{"title":'Track Order',"link":'track-order'},{"title":'Blog',"link":'index'},{"title":'Contact Us',"link":''},{"title":'About Us',"link":'about_us'}]
context = {
        'menu':list_topbar
    }
def main_page(request):
    print("Rendering main page...")
    request.session['session_id']=request.user.id
    print(request.session['session_id'])
    print(request.session.session_key)
    print(request.user)
    if request.user.is_authenticated:
        print("Authenticated User")
        username_text=request.user.username
        hyperlink=''
        # 'logindrpdwn':[['My Account','Log Out']
        return render(request, 'Qwheel_App/index.html', {'menu':list_topbar, 'username':username_text, 'logindrpdwn':[{'content':'My Account', 'link':''},{'content':'Log Out', 'link':'log_out'}] ,'hlink':hyperlink})
    
    else:
        print("Not Logged in")
        username_text='Login'
        hyperlink='account'
        return render(request, 'Qwheel_App/index.html', {'menu':list_topbar, 'username':username_text, 'hlink':hyperlink})
    

    # return render(request, 'Qwheel_App/index.html', {'menu':list_topbar, 'username':username_text})

def about_us_page(request):
    return render(request, 'Qwheel_App/base.html', context)

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
            email=request.POST['email']
            password=request.POST['password']
            user=authenticate(email=email,password=password)
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
                User.objects.create_user(request.POST['email'],request.POST['email'],request.POST['password1'])
            else:
                print("Password 2 didnt matched...")

            return render(request, 'Qwheel_App/account.html', {'form':UserCreationForm, 'form1':AuthenticationForm})

        # if request.POST['login_btn']:
        #     return render(request, 'index.html', {})
        # else:
        #     pass

def addvendor(request):
    request.session['session_id']=request.user.id
    if request.user.is_authenticated:
        username_text=request.user.username
        hyperlink=''
        
    else:
        username_text='Login'
        hyperlink='account'

    if request.method == 'POST':
        form = add_vendor(request.POST or None, request.FILES or None)
        # check whether it's valid:
        if form.is_valid():
            pdb.set_trace()
            details_vendor = form.save(commit=False)
            details_vendor.username = request.user.id
            details_vendor.save()

        else:
            print(form.errors)
                
        # if a GET (or any other method) we'll create a blank form
    else:
        form = add_vendor()
        
    return render(request, 'Qwheel_App/add-vendor.html', {'form': form,'menu':list_topbar, 'username':username_text, 'logindrpdwn':[{'content':'My Account', 'link':''},{'content':'Log Out', 'link':'log_out'}] ,'hlink':hyperlink})
    


    # if request.method == 'POST':
    #     form = add_vendor(request.POST or None, request.FILES or None)
    #     # check whether it's valid:
    #     if form.is_valid():
    #         instance = form.save(commit=False)
    #         instance.user = request.user
    #         print(instance.description)
    #         instance.save()
    #         print("saved vendor!")
    #         pdb.set_trace()
    #     else:
    #         messages.error(request, "Error")
            
    # # if a GET (or any other method) we'll create a blank form
    # else:
    #     form = add_vendor()
    #     # pdb.set_trace()

    return render(request, 'Qwheel_App/add-vendor.html', {'form': form})

def log_out(request):
    print("logging out...")

    if request.method=='GET':
        request.session['session_id']=request.user.id
        del request.session['session_id']
        logout(request)
        
    return redirect(main_page)
    
def addproduct(request):
    request.session['session_id']=request.user.id
    ImageFormSet = modelformset_factory(product_img,form=add_product_img, extra=2)
    if request.user.is_authenticated:
        username_text=request.user.username
        hyperlink=''
        
    else:
        username_text='Login'
        hyperlink='account'
    
    if request.method == 'POST':
            details = add_product(request.POST)
            pics = ImageFormSet(request.POST, request.FILES, queryset=product_img.objects.none())
            # check whether it's valid:
            if details.is_valid() and pics.is_valid():
                details_object = details.save(commit=False)
                details_object.user = request.user
                details_object.save()
                            
                for pic in pics.cleaned_data:
                    if pic:
                        image = pic['image']
                        # pdb.set_trace()
                        photo = product_img(product=details_object, image=image)
                        photo.save()
            else:
                print(details.errors, pics.errors)
                
        # if a GET (or any other method) we'll create a blank form
    else:
        details = add_product()
        pics = ImageFormSet(queryset=product_img.objects.none())

        
    return render(request, 'Qwheel_App/add-product.html', {'form': details,'formset':pics,'menu':list_topbar, 'username':username_text, 'logindrpdwn':[{'content':'My Account', 'link':''},{'content':'Log Out', 'link':'log_out'}] ,'hlink':hyperlink})
        



def shop(request):
    print("Going for Shopping...")

    if request.method=='GET':
        request.session['session_id']=request.user.id
        del request.session['session_id']
        logout(request)
        
    return redirect(main_page)