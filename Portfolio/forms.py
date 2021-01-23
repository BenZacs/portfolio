from django import forms
from .models import Enquiry
from django.forms.widgets import Textarea

class EnquiryForm(forms.ModelForm):
    """ Form for inputing a new event """
    class Meta:
        model = Enquiry
        fields = ['first_name', 'last_name', 'company', 'email']
        first_name = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'first_name'}
            ))
        last_name = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'last_name'}
            ))
        company = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'company'}
        ))
        email = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'email'}
        ))