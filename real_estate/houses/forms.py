from django import forms
from .models import House

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields = [
            'title', 'description', 'property_type', 'status',
            'address',
            'latitude', 'longitude',
            'bedrooms', 'bathrooms', 'square_feet', 'lot_size',
            'year_built', 'floor_number', 'total_floors', 'parking_spaces',
            'price', 'currency', 'hoa_fee', 'property_tax',
            'main_image', 'agent'
        ]

