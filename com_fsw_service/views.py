from django.contrib.auth.models import User
from rest_framework import generics
import simplejson as json
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth import logout
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from com_fsw_models.serializers import *


@api_view(('GET',))
def api_root(request, format=None):
    return Response({

        'user login': reverse('user login', request=request, format=format),
        'user logout': reverse('user logout', request=request, format=format),
        'current user': reverse('current user', request=request, format=format),
        'new user': reverse('new user', request=request, format=format),

        'diets details': reverse('diets-details', request=request, format=format, args="*"),
        'allergies details': reverse('allergies-details', request=request, format=format, args="*"),
        'hospitalization details': reverse('hospitalization-details', request=request, format=format, args="*"),
        'medication details': reverse('medication-details', request=request, format=format, args="*"),
        'assessment details': reverse('assessment-details', request=request, format=format, args="*"),
        'prescription details': reverse('prescription-details', request=request, format=format, args="*"),
        'medicationhistory details': reverse('medicationhistory-details', request=request, format=format, args="*"),
        'emergencycontacts details': reverse('emergencycontacts-details', request=request, format=format, args="*"),
        'notes details': reverse('notes-details', request=request, format=format, args="*"),
        'doctors details': reverse('doctors-details', request=request, format=format, args="*"),
        'residents details': reverse('residents-details', request=request, format=format, args="*"),


    })


def new_user(request):
    try:
        #adds a new user to the django database, note that - django database, not the fsw database!
        username = request.POST['username']
        password = request.POST['password']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        new_entry = User.objects.create_user()
        new_entry.username = username
        new_entry.password = password
        new_entry.first_name = first_name
        new_entry.last_name = last_name
        new_entry.save()
        if new_entry is not None:
            return HttpResponse(json.dumps({'success': '1', 'id': str(new_entry)}), content_type="application/json")
        else:
            return HttpResponse(json.dumps({'success': '0', 'error': 'sql statement was incorrect.'}),
                                content_type="application/json")
    except Exception, e:
        return HttpResponse(json.dumps({'success': '0', 'error': str(e)}), content_type="application/json")


def user_auth(request):
    try:
        #GET is for testing only, change this stuff to POST when we make the login page!
        username = request.GET['username']
        password = request.GET['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #success page
                return HttpResponse(
                    json.dumps({'success': '1', 'username': user.name, 'first_name': user.first_name,
                                'last_name': user.last_name}),
                    content_type="application/json")
            else:
                #nope.jpg
                return HttpResponse(json.dumps({'success': '0', 'error': 'Username is banned.'}),
                                    content_type="application/json")
        else:
            #invalid login
            return HttpResponse(json.dumps({'success': '0', 'error': 'Username or password incorrect.'}),
                                content_type="application/json")
    except:
        return HttpResponse(json.dumps({'success': '0', 'error': 'Incorrect authentication process.'}),
                            content_type="application/json")


def current_user(request):
    if request.user.is_active:
        return HttpResponse(json.dumps({'first_name': request.user.first_name, 'last_name': request.user.last_name,
                                        'username': request.user.username, 'email': request.user.email}),
                            content_type="application/json")
    else:
        return HttpResponse(json.dumps({'success': '0', 'error': 'Username or password incorrect.'}),
                            content_type="application/json")


def user_logout(request):
    logout(request)
    #Note: logout() always returns a true value even if there were no credentials wiped, go figure.
    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")


class DietViewSet(generics.ListCreateAPIView):
    serializer_class = DietSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return Diet.objects.filter(resident_id=q)
        else:
            return Diet.objects.all()


class AllergiesViewSet(generics.ListCreateAPIView):
    serializer_class = AllergySerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return Allergy.objects.filter(resident_id=q)
        else:
            return Allergy.objects.all()


class HospitalizationsViewSet(generics.ListCreateAPIView):
    serializer_class = HospitalizationSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return Hospitalization.objects.filter(resident_id=q)
        else:
            return Hospitalization.objects.all()


class MedicationsViewSet(generics.ListCreateAPIView):
    serializer_class = MedicationSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return Medication.objects.filter(resident_id=q)
        else:
            return Medication.objects.all()


class AssessmentsViewSet(generics.ListCreateAPIView):
    serializer_class = AssessmentSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return Assessment.objects.filter(resident_id=q)
        else:
            return Assessment.objects.all()


class PrescriptionsViewSet(generics.ListCreateAPIView):
    serializer_class = PrescriptionSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return Prescription.objects.filter(resident_id=q)
        else:
            return Prescription.objects.all()


class MedicationHistoryViewSet(generics.ListCreateAPIView):
    serializer_class = MedicationHistorySerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return MedicationHistory.objects.filter(resident_id=q)
        else:
            return MedicationHistory.objects.all()


class EmergencyContactsViewSet(generics.ListCreateAPIView):
    serializer_class = EmergencyContactSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return EmergencyContact.objects.filter(resident_id=q)
        else:
            return EmergencyContact.objects.all()


class NotesViewSet(generics.ListCreateAPIView):
    serializer_class = NotesSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return Notes.objects.filter(resident_id=q)
        else:
            return Notes.objects.all()


class DoctorsViewSet(generics.ListCreateAPIView):
    serializer_class = DoctorSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return Doctor.objects.filter(resident_id=q)
        else:
            return Doctor.objects.all()


class ResidentViewSet(generics.ListCreateAPIView):
    serializer_class = ResidentSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return Resident.objects.filter(resident_id=q)
        else:
            return Resident.objects.all()


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

