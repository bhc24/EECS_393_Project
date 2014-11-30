__author__ = 'stephaniehippo'
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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


class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True)
    passphrase = forms.CharField(widget=forms.PasswordInput(), required=True)
    confirm_passphrase = forms.CharField(widget=forms.PasswordInput(), required=True)

    def __init__(self, *args, **kwargs):
        super(UserCreationForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = ['username', 'password1', 'password2']

    def verify_passphrase(self):
        passphrase1 = self.cleaned_data.get('passphrase')
        passphrase2 = self.cleaned_data.get('confirm_passphrase')

        if(passphrase1 != passphrase2):
            raise forms.ValidationError("Passphrases do not match")

        return True

    def clean(self, *args, **kwargs):
        cleaned_data = super(UserCreationForm, self).clean()

        return cleaned_data

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit)

        if user:
            user.username=self.cleaned_data['username']
            user.set_password(self.cleaned_data['passphrase'])

            if commit:
                user.save()

        return user