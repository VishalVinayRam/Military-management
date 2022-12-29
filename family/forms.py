from django import forms
from .models import Family

class RegimentForm(forms.ModelForm):
    
    class Meta:
        model = Family
        fields = '__all__'