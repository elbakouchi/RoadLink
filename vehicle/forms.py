from django import forms
from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ('registration_plate', 'mileage', 'vehicle_type', 'fuel_type', 'insurance_status', 'image')
