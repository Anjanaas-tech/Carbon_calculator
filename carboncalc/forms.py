from django import forms
from .models import CarbonFootprintEntry

class CarbonFootprintForm(forms.ModelForm):
    class Meta:
        model = CarbonFootprintEntry
        fields = ['name', 'transport', 'electricity', 'diet']
