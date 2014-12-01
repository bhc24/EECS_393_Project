from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import auth, sessions
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from pamlla.forms import NewPatientForm, LoginForm, SignUpForm
from pamlla.models import Patient, User, Doctor, Prediction, Logit, HazardFunction, MutatedGenes, SurvivalFactors
# Create your views here.

@login_required(login_url='/login/')
def patients(request):
    patient_list = Patient.objects.all()
    return render(request, "Patient_List.html", {'patient_list': patient_list})

@login_required(login_url='/login/')
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
            return HttpResponseRedirect('/patient_list/')
    form=NewPatientForm(
        initial={'username': "User Name", 'patient_name': "Patient Name"}
    )
    return render(request, "New_Patient.html", {'form':form})

@login_required(login_url='/login/')
def history(request):
    #Get all histories for a particular patient
    return render(request, "Patient_History.html")

def login_view(request):

    auth.logout(request)
    if 'sign_up' in request.POST:
        return HttpResponseRedirect("/signup/")

    form = LoginForm(request.POST or None)

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login(request)

            if user:
                auth.login(request, user)
                sessions.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                return HttpResponseRedirect("/patient_list/")

    return render(request, 'index.html', {'form': form})


def home(request):
    return render(request, "index.html")

def signup_view(request):

    print(request.POST)
    print()
    print()
    print()

    form = SignUpForm(request.POST or None)

    if request.POST:
        form = SignUpForm(request.POST)

        if form.is_valid():

            if form.verify_passphrase():
                user = form.add_user(request)

                if user:

                    auth.login(request, user)
                    return HttpResponseRedirect("/patient_list/")
                else:
                    print("blank user")
            else:
                print("mismatched passphrase")
        else:
            print("invalid form")

    return render(request, "Sign_Up.html", {'form': form,})
