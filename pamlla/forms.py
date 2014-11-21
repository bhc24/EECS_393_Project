__author__ = 'stephaniehippo'
from django import forms
from django.contrib import auth

class NewPatientForm(forms.Form):
    username = forms.CharField(label="User Name")
    patient_name = forms.CharField(label="Patient Name")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")


class LoginForm(forms.Form):
    username = forms.CharField(label="User Name")
    password = forms.CharField(widget=forms.PasswordInput(), label="Password")

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data


    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = auth.authenticate(username=username, password=password)
        return user