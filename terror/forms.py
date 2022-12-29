from django import forms
from .models import Terrorist

class TerrorstForm(forms.ModelForm):
    
    class Meta:
        model = Terrorist
        fields = ['name', 'place' , 'id' , 'Mission_captured','father_name','is_alive' ]
        labels = {'name' : "Name" , 'place':"Place" , 'id' : "Id" , 'Mission_captured' : "Mission_captured" , 'father_name' : "Father_name" , 'is_alive' : "Is_Alive"}

   