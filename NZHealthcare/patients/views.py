from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Patient, Referral
from .forms import PatientForm, ReferralForm

# Create your views here.


def home(request):
    return render(request, 'home.html')


def login(request):
    return render(request, 'login.html')


@login_required
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})


@login_required
def add_patient(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            patient = form.save()
            return render(request, 'patient_detail.html', {'patient': patient})
    else:
        form = PatientForm()

    return render(request, 'add_patient.html', {'form': form})


@login_required
def referrals_list(request):
    referrals = Referral.objects.all()
    return render(request, 'referrals_list.html', {'referrals': referrals})


@login_required
def add_referral(request):
    if request.method == 'POST':
        form = ReferralForm(request.POST)
        if form.is_valid():
            referral = form.save()
            return render(request, 'referral_detail.html', {'referral': referral})
    else:
        form = ReferralForm()

    return render(request, 'add_referral.html', {'form': form})


@login_required
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, id=patient_id)
    referrals = Referral.objects.filter(patient=patient)
    return render(request, 'patient_detail.html', {'patient': patient, 'referrals': referrals})


@login_required
def referral_detail(request, referral_id):
    referral = get_object_or_404(Referral, id=referral_id)
    return render(request, 'referral_detail.html', {'referral': referral})
