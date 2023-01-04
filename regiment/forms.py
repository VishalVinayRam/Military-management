from django import forms
from .models import Regiment

class RegimentForm(forms.ModelForm):
    
    class Meta:
        model = Regiment
        fields = '__all__'