from django import forms
from . models import Customers

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class UserRegisterationForm(forms.ModelForm):
    class Meta:
        model = Customers
        fields = ('name' , 'city', 'contact', 'email', 'password')
