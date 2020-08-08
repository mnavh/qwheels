from django import forms
from .models import vendor, product

class add_vendor(forms.ModelForm):
    class Meta:
        model = vendor
        fields = ['name','description','logo','address','email','contact']

class add_product(forms.ModelForm):
    class Meta:
        model = product
        fields = ['vendor','category','subcategory','name','price','description','specifications','brand','sku','availability']