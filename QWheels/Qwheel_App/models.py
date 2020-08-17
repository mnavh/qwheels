from django.db import models
from django.contrib.auth.models import AbstractUser

Categories = (
    ('A', 'Admin'),
    ('V', 'Vendor'),
    ('U', 'User')
)

class User(AbstractUser):
    user_role = models.CharField(max_length=10, choices=Categories, default='U')
    pass 

# Create your models here.
class vendor(models.Model):
    username = models.ForeignKey(User, default = 1, on_delete=models.CASCADE)
    name = models.CharField(max_length=25, blank=True, null=True)
    description = models.CharField(max_length=25, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True)
    address = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(unique=True,blank=True, null=True)
    contact = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.name

class product(models.Model):
    username = models.ForeignKey(User, default = 1, on_delete=models.CASCADE)
    vendor = models.ForeignKey(vendor, on_delete=models.CASCADE, blank=True, null=True)
    category = models.CharField(max_length=25, blank=True, null=True)
    subcategory = models.CharField(max_length=25, blank=True, null=True)
    name = models.CharField(max_length=25, blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=2500,blank=True, null=True)
    specifications = models.CharField(max_length=2500,blank=True, null=True)
    brand = models.CharField(max_length=25, blank=True, null=True)
    sku = models.CharField(max_length=25,blank=True, null=True)
    availability = models.BooleanField(default=True,blank=True, null=True)
    
    def __str__(self):
        return self.name

class product_img(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.product