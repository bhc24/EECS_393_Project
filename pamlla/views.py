from django.shortcuts import render
from django.contrib import auth, sessions
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, loader
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from pamlla.forms import NewPatientForm, LoginForm, UserForm, UserProfileForm
from pamlla.models import UserProfile, Patient, Doctor, Prediction, Logit, HazardFunction, MutatedGenes, SurvivalFactors
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
            user_profile=UserProfile(user=user, name=cd['patient_name'], isPatient=True, isDoctor=False)
            user_profile.save()
            user=User.objects.get(request.user.user_id)
            doctor_profile = UserProfile.get(user=user)
            doctor = Doctor.get(doctor_profile)
            new_patient=Patient(name=cd['patient_name'], patient=user_profile, doctor=doctor)
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


def register(request):
    errors = []
    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            registered = True
            if profile.isDoctor and not profile.isPatient:
                profile.save()
                new_doctor=Doctor(name=profile.name, doctor=profile)
                new_doctor.save()
           #     mygroup, created = Group.objects.get_or_create(name=user.username)
                return HttpResponseRedirect('/patient_list/')
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'Sign_Up.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered, 'errors': errors})

def logout_view(request):
    auth.logout(request)
    return render(request, 'Log_Out.html')

