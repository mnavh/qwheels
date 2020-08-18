from django import forms
from .models import vendor, product, product_img, User
from django.utils.translation import ugettext, ugettext_lazy as _

class UserCreationForm(forms.ModelForm):
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput)
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput,
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ("user_role","email",)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

class add_vendor(forms.ModelForm):
    class Meta:
        model = vendor
        fields = ['name','description','logo','address','contact']

class add_product(forms.ModelForm):
    class Meta:
        model = product
        fields = ['vendor','category','subcategory','name','price','description','specifications','brand','sku','availability']

class add_product_img(forms.ModelForm):
    image = forms.ImageField(label='Image')    
    class Meta:
        model = product_img
        fields = ('image', )
