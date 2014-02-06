# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext


def index(request):
    return render_to_response('index.html',
                              context_instance=RequestContext(request))


def user_auth(request):
    return render_to_response('user_auth.html')


def allergies(request):
    return render_to_response('allergies.html')


def diet(request):
    return render_to_response('diet.html')


def hospitalizations(request):
    return render_to_response('hospitalizations.html')


def medications(request):
    return render_to_response('medications.html')


def assessments(request):
    return render_to_response('assessments.html')


def prescriptions(request):
    return render_to_response('prescriptions.html')


def medication_history(request):
    return render_to_response('medication_history.html')


def emergency_contacts(request):
    return render_to_response('emergency_contacts.html')


def notes(request):
    return render_to_response('notes.html')


def doctors(request):
    return render_to_response('doctors.html')


def patients(request):
    return render_to_response('patients.html')