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


class SignUpForm(forms.Form):
    name = forms.CharField(label="Name")
    username = forms.CharField(label="User Name")
    passphrase1 = forms.CharField(widget=forms.PasswordInput(), label="passphrase")
    passphrase2 = forms.CharField(widget=forms.PasswordInput(), label="confirm passphrase")

    def verify_passphrase(self, request):
        passphrase1 = self.cleaned_data.get('passphrasae')
        passphrase2 = self.cleaned_data.get('confirm passphrase')
        if(passphrase1 != passphrase2):
            raise forms.ValidationError("Passphrases do not match")
        return self.cleaned_data

    def add_user(self, request):
        name = self.cleaned_data.get('name')
        username = self.cleaned_data('username')
        passphrase = self.cleaned_data

