from django import forms
from .models import Regiment

class RegimentForm(forms.ModelForm):
    
    class Meta:
        model = Regiment
        fields = '__all__'
        # labels = {'name' : "Name" , 'place':"Place" , 'id' : "Id" , 'Mission_captured' : "Mission_captured" , 'father_name' : "Father_name" , 'is_alive' : "Is_Alive"}

   