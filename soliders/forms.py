from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from soliders.models import *

class MyForm(forms.ModelForm):
  class Meta:
    model = UserModel
    fields = ["name", "password","email",]
    labels = {'name': "Name", "mobile_number": "Mobile Number","email":"email"}
    # widget ={
    #   'name':  forms.TextField(attrs={'class':'form-control'}),
    #   'password':forms.PasswordInput(attrs={'class':'form-control'}),

    # }

class UserRegisterForm(UserCreationForm):

    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email' , 'password1', 'password2']

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {'username': "Username", "password": "Password"},
    #     widget ={
    #   'name':  forms.TextField(attrs={'class':'form-control'}),
    #   'password':forms.PasswordInput(attrs={'class':'form-control'}),

    # }
class SoliderForm(forms.ModelForm):
    class Meta:
        model = Soliders
        fields = ['name','post']
