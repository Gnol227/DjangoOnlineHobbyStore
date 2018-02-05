from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class RegisterForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50)
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Re-Enter Password", widget=forms.PasswordInput())

    def clean_password2(self):
        if 'password1' in self.cleaned_data: #check if user has entered pass1
            password1 = self.cleaned_data['password1'] #get pass1
            password2 = self.cleaned_data['password2']
            if password1 == password2:
                return password2
        raise forms.ValidationError("Invalid password!")

    def clean_username(self): #avoid user to use special character
        username = self.cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError("Invalid username - no special character(s)!")
        try:
            User.objects.get(username=username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError("Username has exist!")

