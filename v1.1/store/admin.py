from django.contrib import admin
from .models import *
# Register your models here.


myModel =[Product, Category]

admin.site.register(myModel)