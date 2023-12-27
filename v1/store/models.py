from django.db import models
from accounts.models import Vendor

# Create your models here.
class Category(models.Model):
    name = models.TextField(max_length=99, null=True)

    def __str__(self):
        return f"{self.name}"



class Product(models.Model):
    product_name = models.CharField(max_length=200)
    product_vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=99999, decimal_places=2)
    product_description = models.CharField(max_length=1000, blank=True, null=True)
    product_info = models.CharField(max_length=100000, blank=True, null=True)
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    product_image = models.ImageField(upload_to='uploads')
    quanitity = models.PositiveBigIntegerField()
    digital = models.BooleanField(default=False)
    image1 = models.ImageField(upload_to='uploads', blank=True, null=True)
    image2 = models.ImageField(upload_to='uploads', blank=True, null=True)
    image3 = models.ImageField(upload_to='uploads', blank=True, null=True)
    image4 = models.ImageField(upload_to='uploads', blank=True, null=True)
    image5 = models.ImageField(upload_to='uploads', blank=True, null=True)
    image6 = models.ImageField(upload_to='uploads', blank=True, null=True)
    


    def __str__(self):
        return f"{self.product_name}"