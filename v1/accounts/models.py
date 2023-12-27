from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Vendor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField(max_length=100)
    about_us = models.CharField(max_length=10000, blank=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    certified = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name
