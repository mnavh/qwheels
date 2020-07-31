from QWheels.urls import path
from Qwheel_App import views
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views


urlpatterns=[
    path('',views.main_page, name="main_page"),
    path('main_page_html',views.main_page, name="main_page"),
    path('deals',views.deals_page, name="deals_page"),
    # path('account',views.account_page, name="account_page"),
    # path('account', auth_views.LoginView.as_view(template_name="account.html"), name='account_page'),
    path('account', views.account_page, name='account_page'),
   
    
    
]




