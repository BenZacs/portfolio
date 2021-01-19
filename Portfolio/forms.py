  
from django import forms
from .models import Info
from django.forms.widgets import Textarea

class InfoForm(forms.ModelForm):
    """ Form for inputing a new event """
    class Meta:
        model = Info
        fields = ['photo', 'first_name', 'last_name', 'address', 'about_me',
        'interest', 'phone_number', 'high_school', 'high_school_gpa',
        'university', 'department', 'faculty', 'university_gpa']
        photo = forms.ImageField()
        first_name = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'first_name'}
            ))
        last_name = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'last_name'}
            ))
        address = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'address'}
            ))
        about_me = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'about_me'}
            ))
        interest = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'interest'}
            ))
        phone_number = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'phone_number'}
            ))
        high_school = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'number-people'}
            ))
        high_school_gpa = forms.FloatField(required=True, max_value=4, min_value=0, 
            widget=forms.NumberInput(
            attrs={'id': 'high_school_gpa', 'step': "0.01"}))
        university = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'university'}
            ))
        department = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'department'}
            ))
        faculty = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'faculty'}
            ))
        university_gpa = forms.FloatField(required=True, max_value=4, min_value=0, 
            widget=forms.NumberInput(
            attrs={'id': 'university_gpa', 'step': "0.01"}))