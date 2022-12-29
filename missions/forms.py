from django import forms
from .models import Mission

class RegimentForm(forms.ModelForm):
    
    class Meta:
        model = Mission
        fields = '__all__'