from django import forms
from django.contrib.auth import authenticate
from .models import *

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, label='Remember Me',widget=forms.CheckboxInput(attrs={'class': 'box'}))

    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise forms.ValidationError("This user doesn't exist")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("User no longer Active")
        return super(LoginForm,self).clean(*args,**kwargs)
