from django import forms
from django.contrib.auth.models import User

from soliders.models import UserModel

class MyForm(forms.ModelForm):
  class Meta:
    model = UserModel
    fields = ["name", "password","email",]
    labels = {'name': "Name", "mobile_number": "Mobile Number","email":"email"}



class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {'username': "Username", "password": "Password"}