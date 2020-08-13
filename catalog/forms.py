from django import forms

class NameForm(forms.Form):
    client_name = forms.CharField(label='your_name', max_length=100)