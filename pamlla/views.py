from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
# Create your views here.


def patients(request):
    return render(request, "Patient_List.html")

def add_patient(request):
    return render(request, "New_Patient.html")

def history(request):
    return render(request, "Patient_History.html")

def login(request):
    return render(request, "Sign_Up.html")

def home(request):
    return render(request, "index.html")