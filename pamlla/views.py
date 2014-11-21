from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from pamlla.forms import NewPatientForm, LoginForm
from pamlla.models import Patient, User, Doctor, Prediction, Logit, HazardFunction, MutatedGenes, SurvivalFactors
# Create your views here.


def patients(request):
    patient_list = Patient.objects.all()
    return render(request, "Patient_List.html", {'patient_list': patient_list})

def add_patient(request):
    errors = []
    name = None
    username = None
    password = None
    if request.method == 'POST':
        form = NewPatientForm(request.POST)
        #Check existence of patient name
        if form.is_valid():
            cd = form.cleaned_data
            user = User(username=cd['username'], passphrase=cd['password'])
            user.save()
            new_patient=Patient(name=cd['patient_name'], patient=user)
            new_patient.save()
        return HttpResponseRedirect('/patients/')
    form=NewPatientForm(
        initial={'username': "User Name", 'patient_name': "Patient Name"}
    )
    return render(request, "New_Patient.html", {'form':form})

def history(request):
    #Get all histories for a particular patient
    return render(request, "Patient_History.html")

def login_view(request):
    form = LoginForm(request.POST or None)

    if 'sign_up' in request.POST:
        return HttpResponseRedirect("/signup/")

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)

            if user:
                auth.login(request, user)
                return HttpResponseRedirect("/patient_list/")

    return render(request, 'index.html', {'login_form': form})


def home(request):
    return render(request, "index.html")

def signup(request):

    return render(request, "Sign_Up.html")
