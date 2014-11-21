__author__ = 'stephaniehippo'
from django import forms

class NewPatientForm(forms.Form):
    username = forms.CharField()
    patient_name = forms.CharField()
    password = forms.PasswordInput()