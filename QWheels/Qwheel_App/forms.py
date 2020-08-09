from django import forms
from .models import vendor, product, product_img

class add_vendor(forms.ModelForm):
    class Meta:
        model = vendor
        fields = ['name','description','logo','address','email','contact']

class add_product(forms.ModelForm):
    class Meta:
        model = product
        fields = ['vendor','category','subcategory','name','price','description','specifications','brand','sku','availability']

class add_product_img(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = product_img
        fields = ('image', )
