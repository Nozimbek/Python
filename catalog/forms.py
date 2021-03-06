from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['client_name']

class CheckingForm(forms.Form):
    secret_number = forms.CharField()
    client_name = forms.CharField()
