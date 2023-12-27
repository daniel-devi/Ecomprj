from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from .models import *

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class VendorProductForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(VendorProductForm, self).__init__(*args, **kwargs)
        if self.user:
            self.fields['user'].initial = self.user
            self.fields['user'].widget = forms.HiddenInput()