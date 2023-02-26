from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from soliders.models import *


    #   'name':  forms.TextField(attrs={'class':'form-control'}),
    #   'password':forms.PasswordInput(attrs={'class':'form-control'}),

    # }

class Join_Amry_Form(forms.ModelForm):
    class  Meta:
        model = Join_Army
        fields = ['name','father_name','mother_name','dob','address','contact','email','date']


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
        model = Soliders_register
        fields = ['name','father_name','address','dob','contact','email','date']



class Letter_form(forms.ModelForm):
    class Meta:
        model = Leave_Letter_Form
        fields = ['sol_id','leave_type','leave_from','leave_to','reason','address','contact','date']
        labels = {"sol_id": "Soldier Id","leave_type":"Leave Type","leave_from":"Leave From","leave_to":"Leave To","reason":"Reason","address":"Address","contact":"Contact","date":"Date"}
        # widget ={
        #   'name':  forms.TextField(attrs={'class':'form-control'}),
        #   'password':forms.PasswordInput(attrs={'class':'form-control'}),

        # }
class CreateUserForm(UserCreationForm):
    # sol_id  = .AutoField(null=False)
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']