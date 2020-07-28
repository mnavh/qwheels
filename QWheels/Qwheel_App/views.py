from django.shortcuts import render


# Create your views here.

def main_page(request):
    return render(request, 'index.html', {})

def deals_page(request):
    return render(request, 'deals.html', {})

def account_page(request):
    return render(request, 'account.html', {})




