__author__ = 'stephaniehippo'
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User
from pamlla.models import UserProfile


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

# 1. Create the two forms to be used with the view
# 1.1 Meta adds extra information about the user and user profile
# 1.2 I'm a little shakey on how forms work
# 2. Go to views.py

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

class UserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ('isDoctor', 'isPatient')