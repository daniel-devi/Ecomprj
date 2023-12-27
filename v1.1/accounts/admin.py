from django.contrib import admin
from accounts.models import *

# Register your models here.
myModels = [Vendor] # iterable list
admin.site.register(myModels)