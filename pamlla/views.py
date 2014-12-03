from django.shortcuts import render
from django.contrib import auth, sessions
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from pamlla.forms import NewPatientForm, LoginForm, UserForm, DocumentForm
from pamlla.models import UserProfile, Patient, Doctor, Prediction, Document
# Create your views here.


@login_required(login_url='/login/')
def patients(request):
    #user=User.objects.get(id=request.user)
    doctor_profile = UserProfile.objects.get(user=request.user)
    doctor = Doctor.objects.get(doctor=doctor_profile)
    patient_list = Patient.objects.filter(doctor=doctor)
    return render(request, "Patient_List.html", {'patient_list': patient_list})


@login_required(login_url='/login/')
def add_patient(request):

    if request.method == 'POST':
        form = NewPatientForm(request.POST)
        # Check existence of patient name
        if form.is_valid():
            cd = form.cleaned_data
            user = User(username=cd['username'], first_name=cd['first_name'], last_name=cd['last_name'])
            user.set_password(cd['password'])
            user.save()
            user_profile=UserProfile(user=user)
            user_profile.save()
            user=User.objects.get(id=request.user.id)
            doctor_profile = UserProfile.objects.get(user=request.user)
            doctor = Doctor.objects.get(doctor=doctor_profile)
            new_patient=Patient(patient=user_profile, doctor=doctor)
            new_patient.save()
            return HttpResponseRedirect('/patient_list/')
    form=NewPatientForm(
        initial={'username': "User Name", 'patient_name': "Patient Name"}
    )
    return render(request, "New_Patient.html", {'form':form})


@login_required(login_url='/login/')
def history(request, patient_id):
    user=User.objects.get(id=request.user.id)
    # Assume its a doctor?
    user=User.objects.get(id=request.user.id)
    profile = UserProfile.objects.get(user=user)

    patient = Patient.objects.get(id=patient_id)
    patient_list = []
    predictions = []
    # get request comes with patient id
    # Check if the doctor or patient has permission to view this id
    if 'patient_id' in request.GET:
        if profile.isDoctor:
            doctor = Doctor.objects.get(doctor=profile)
            patient_list = Patient.objects.filter(doctor=doctor)
        elif profile.isPatient:
            am_i_a_patient = Patient.objects.get(patient=profile)
            if am_i_a_patient.id == patient_id:
                patient_list = Patient.objects.filter(patient_id=patient_id)
        if patient in patient_list:
            # Authorized.
            predictions = Prediction.filter(patient=patient)
            # for patient in patient_list:
                # Get all predictions for a particular patient
                # Get all Data Sets for each history
        # else:
            # TODO: No permission to view, Force Logout?
    return render(request, "Patient_History.html", {'predictions':predictions})


def login_view(request):

    logout(request)

    if 'sign_up' in request.POST:
        return HttpResponseRedirect("/signup/")

    form = LoginForm(request.POST or None)

    if request.POST:
        print "It's a login post"
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.login()
            print "Login form was valid"
            if user:
                auth.login(request, user)
                sessions.SESSION_EXPIRE_AT_BROWSER_CLOSE = True
                return HttpResponseRedirect("/patient_list/")
        else:
            print "Login form was not valid :("
    return render(request, 'index.html', {'form': form})


def home(request):
    return render(request, "index.html")


def register(request):
    errors = []
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user_cd = user_form.cleaned_data
            user = User(username=user_cd['username'],first_name=user_cd['first_name'], last_name=user_cd['last_name'])
            print 'This is the password'
            print user_cd['password']
            user.set_password(user_cd['password'])
            print user.password
            user.save()
            user_profile = UserProfile(user=user)
            user_profile.save()
            registered = True
            new_doctor = Doctor(doctor=user_profile)
            new_doctor.save()
            return HttpResponseRedirect('/patient_list/')
    else:
        user_form = UserForm()

    return render(request, 'Sign_Up.html', {'user_form': user_form, 'registered': registered, 'errors': errors})


def logout_view(request):
    auth.logout(request)
    return render(request, 'Log_Out.html')


def analyze(request):

    if request.method == 'POST':
        analyze_form = DocumentForm(request.POST, request.FILES)

        if analyze_form.is_valid():
            for docfile in request.FILES:
                newdoc = Document(docfile = request.FILES[docfile])
                newdoc.save()

    else:
        analyze_form = DocumentForm()

    documents = Document.objects.all()

    return render(request, 'Patient_Analyze.html', {'documents': documents, 'form': analyze_form})

