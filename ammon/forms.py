from django import forms
from .models import Ammo

class RegimentForm(forms.ModelForm):
    
    class Meta:
        model = Ammo
        fields = '__all__'