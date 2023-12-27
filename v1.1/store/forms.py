from django import forms
from .models import *

    
class CreateProduct(forms.ModelForm):
    class Meta :
        model = Product
        exclude = ['product_vendor']
        fields = '__all__'