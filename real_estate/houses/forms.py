from django import forms
from .models import House

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = ['title', 'address', 'price', 'status', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
        }
