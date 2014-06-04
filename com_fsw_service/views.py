from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
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
        'residents to doctor details': reverse('residents-to-doctor-details', request=request, format=format, args="*"),
        'physical details': reverse('physical-details', request=request, format=format, args="*"),
        'insurance details': reverse('insurance-details', request=request, format=format, args="*"),
        'alert details': reverse('alert-details', request=request, format=format, args="*"),
        'document details': reverse('document-details', request=request, format=format, args="*"),
        'subscriptions details': reverse('subscriptions-details', request=request, format=format, args="*"),

    })


@method_decorator(csrf_exempt)
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


@method_decorator(csrf_exempt)
def user_auth(request):
    try:
        #GET is for testing only, change this stuff to POST when we make the login page!
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #success page
                return HttpResponse(
                    json.dumps({'success': '1', 'username': user.username, 'first_name': user.first_name,
                                'last_name': user.last_name, 'last_login': user.last_login, 'is_staff': user.is_staff},
                               default=date_handler),
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


@method_decorator(csrf_exempt)
def current_user(request):
    if request.user.is_active:
        return HttpResponse(json.dumps({'first_name': request.user.first_name, 'last_name': request.user.last_name,
                                        'username': request.user.username, 'email': request.user.email,
                                        'last_login': request.user.last_login, 'is_staff': request.user.is_staff},
                                       default=date_handler),
                            content_type="application/json")
    else:
        return HttpResponse(json.dumps({'success': '0', 'error': 'Username or password incorrect.'}),
                            content_type="application/json")


def user_logout(request):
    logout(request)
    #Note: logout() always returns a true value even if there were no credentials wiped, go figure.
    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")


@method_decorator(csrf_exempt)
def edit(request):
    if (request.method == "POST"):
        #get the variables
        res_id = request.POST['resident_id']
        row_id = request.POST['row_id']
        user_id = request.POST['user_id']
        date_time = request.POST['date_time']
        edit_message = request.POST['edit_message']
        type = request.POST['type']
        #type def:
        #0 = resident
        #5 = doctor (note resident_id == doctor_id)
        if (type):
            if (type == "0"):
                #edit the resident
                try:
                    #update the resident based on post vars
                    resident = Resident.objects.get(resident_id=res_id)
                    resident.first_name = request.POST['first_name']
                    resident.middle_name = request.POST['middle_name']
                    resident.last_name = request.POST['last_name']
                    resident.address1 = request.POST['address1']
                    resident.address2 = request.POST['address2']
                    resident.city = request.POST['city']
                    resident.state = request.POST['state']
                    resident.zip_code = request.POST['zip_code']
                    resident.home_phone = request.POST['home_phone']
                    resident.cell_phone = request.POST['cell_phone']
                    resident.date_of_birth = request.POST['date_of_birth']
                    resident.photo = request.POST['photo']
                    if(request.POST['flu_shot'] == "null"):
                         resident.flu_shot = None
                    else:
                         resident.flu_shot = request.POST['flu_shot']
                    if(request.POST['dnr'] == "0"):
                         resident.dnr = False
                    else:
                         resident.dnr = True
                    #save it
                    resident.save()
                    #create a new alert
                    new_alert = Alerts(resident_id=res_id, username=user_id, general_text=edit_message, flag=0,
                                       date_time_modified=date_time, type=1)
                    new_alert.save()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
            if (type == "5"):
                #edit the resident
                try:
                    #update the resident based on post vars
                    #doctor_id = row_id from form!
                    doctor = Doctor.objects.get(doctor_id=row_id)
                    doctor.first_name = request.POST['first_name']
                    doctor.middle_name = request.POST['middle_name']
                    doctor.last_name = request.POST['last_name']
                    doctor.specialization = request.POST['specialization']
                    doctor.phone_number = request.POST['phone_number']
                    #save it
                    doctor.save()
                    #create a new alert
                    new_alert = Alerts(resident_id=res_id, username=user_id, general_text=edit_message, flag=0,
                                       date_time_modified=date_time, type=1)
                    new_alert.save()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
    if (request.method == "GET"):
        return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")


@method_decorator(csrf_exempt)
def delete(request):
    if (request.method == "POST"):
        #get the variables
        res_id = request.POST['resident_id']
        row_id = request.POST['row_id']
        user_id = request.POST['user_id']
        date_time = request.POST['date_time']
        delete_message = request.POST['delete_message']
        type = request.POST['type']
        #type def:
        #0 = resident
        #1 = medication
        #2 = medication_history
        #3 = assessment
        #4 = insurance
        #5 = doctor (note resident_id == doctor_id)
        #6 = prescription
        #7 = hospitalization
        #8 = emergency_contact
        #9 = alert
        #10 = physical
        #11 = note
        #12 = diet
        #13 = allergies
        #14 = unlink doctor to resident
        if (type):
            if (type == "0"):
                #delete the resident
                try:
                    Resident.objects.filter(resident_id=res_id).delete()
                    #delete all links to this resident
                    #delete all resident_to_doctor links
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
            if (type == "1"):
                #delete the medication
                try:
                    #we only care about the row_id which equals the medication_id
                    Medication.objects.filter(medication_id=row_id).delete()
                    #create a new alert
                    new_alert = Alerts(resident_id=res_id, username=user_id, general_text=delete_message, flag=0,
                                       date_time_modified=date_time, type=1)
                    new_alert.save()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
            if (type == "2"):
                #delete the medication history
                try:
                    #we only care about the row_id which equals the medication_id
                    MedicationHistory.objects.filter(medication_id=row_id).delete()
                    #create a new alert
                    new_alert = Alerts(resident_id=res_id, username=user_id, general_text=delete_message, flag=0,
                                       date_time_modified=date_time, type=1)
                    new_alert.save()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
            if (type == "3"):
                #delete the assessment
                try:
                    #we only care about the row_id which equals the assessment_id
                    Assessment.objects.filter(assessment_id=row_id).delete()
                    #create a new alert
                    new_alert = Alerts(resident_id=res_id, username=user_id, general_text=delete_message, flag=0,
                                       date_time_modified=date_time, type=1)
                    new_alert.save()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
            if (type == "4"):
                #delete the insurance
                try:
                    #we only care about the row_id which equals the insurance_id
                    Insurance.objects.filter(insurance_id=row_id).delete()
                    #create a new alert
                    new_alert = Alerts(resident_id=res_id, username=user_id, general_text=delete_message, flag=0,
                                       date_time_modified=date_time, type=1)
                    new_alert.save()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
            if (type == "5"):
                #delete the doctor (before he regenerates!)
                try:
                    #res_id = doctor_id
                    Doctor.objects.filter(doctor_id=res_id).delete()
                    #delete all resident_to_doctor links
                    ResidentToDoctor.objects.filter(doctor_id=res_id).delete()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
            if (type == "6"):
                #delete the prescription
                try:
                    #we only care about the row_id which equals the prescription_number
                    Prescription.objects.filter(prescription_number=row_id).delete()
                    #create a new alert
                    new_alert = Alerts(resident_id=res_id, username=user_id, general_text=delete_message, flag=0,
                                       date_time_modified=date_time, type=1)
                    new_alert.save()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
            if (type == "7"):
                #delete the hospitalization
                try:
                    #we only care about the row_id which equals the hospitalization_id
                    Hospitalization.objects.filter(hospitalization_id=row_id).delete()
                    #create a new alert
                    new_alert = Alerts(resident_id=res_id, username=user_id, general_text=delete_message, flag=0,
                                       date_time_modified=date_time, type=1)
                    new_alert.save()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
            if (type == "8"):
                #delete the emergency contact
                try:
                    #we only care about the row_id which equals the em_id
                    EmergencyContact.objects.filter(em_id=row_id).delete()
                    #create a new alert
                    new_alert = Alerts(resident_id=res_id, username=user_id, general_text=delete_message, flag=0,
                                       date_time_modified=date_time, type=1)
                    new_alert.save()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
            if (type == "9"):
                #You cannot actually delete an alert, but this will update it's flag to 1
                try:
                    #we only care about the row_id which equals the alert_id
                    Alerts.objects.filter(alert_id=row_id).update(flag=1)
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
            if (type == "10"):
                #delete the physical information
                try:
                    #we only care about the row_id which equals the physical_id
                    Physical.objects.filter(physical_id=row_id).delete()
                    #create a new alert
                    new_alert = Alerts(resident_id=res_id, username=user_id, general_text=delete_message, flag=0,
                                       date_time_modified=date_time, type=1)
                    new_alert.save()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
                    #if(type == "11"):
                    #notes don't have an ID number
            if (type == "12"):
                #delete the diet
                try:
                    #we only care about the row_id which equals the diet_id
                    Diet.objects.filter(diet_id=row_id).delete()
                    #create a new alert
                    new_alert = Alerts(resident_id=res_id, username=user_id, general_text=delete_message, flag=0,
                                       date_time_modified=date_time, type=1)
                    new_alert.save()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
            if (type == "13"):
                #delete the allergy
                try:
                    #we only care about the row_id which equals the allergy_id
                    Allergy.objects.filter(allergy_id=row_id).delete()
                    #create a new alert
                    new_alert = Alerts(resident_id=res_id, username=user_id, general_text=delete_message, flag=0,
                                       date_time_modified=date_time, type=1)
                    new_alert.save()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
            if (type == "14"):
                #Unlink a doctor from a resident
                try:
                    ResidentToDoctor.objects.filter(resident_id=res_id, doctor_id=row_id).delete()
                    #create a new alert
                    new_alert = Alerts(resident_id=res_id, username=user_id, general_text=delete_message, flag=0,
                                       date_time_modified=date_time, type=1)
                    new_alert.save()
                    return HttpResponse(json.dumps({'success': '1'}), content_type="application/json")
                except:
                    return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")
    if (request.method == "GET"):
        return HttpResponse(json.dumps({'success': '0'}), content_type="application/json")


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
        q = self.kwargs['doctor_id']
        if q != '*':
            return Doctor.objects.filter(doctor_id=q)
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


class ResidentToDoctorViewSet(generics.ListCreateAPIView):
    serializer_class = ResidentToDoctorSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return ResidentToDoctor.objects.filter(resident_id=q)
        else:
            return ResidentToDoctor.objects.all()


class PhysicalViewSet(generics.ListCreateAPIView):
    serializer_class = PhysicalSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return Physical.objects.filter(resident_id=q)
        else:
            return Physical.objects.all()


class InsuranceViewSet(generics.ListCreateAPIView):
    serializer_class = InsuranceSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return Insurance.objects.filter(resident_id=q)
        else:
            return Insurance.objects.all()


class DocumentStorageViewSet(generics.ListCreateAPIView):
    serializer_class = DocumentStorageSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return DocumentStorage.objects.filter(resident_id=q)
        else:
            return DocumentStorage.objects.all()


class AlertsViewSet(generics.ListCreateAPIView):
    serializer_class = AlertsSerializer

    def get_queryset(self):
        q = self.kwargs['resident_id']
        if q != '*':
            return Alerts.objects.filter(resident_id=q)
        else:
            return Alerts.objects.all()


class SubscriptionViewSet(generics.ListCreateAPIView):
    serializer_class = SubscriptionsSerializer

    def get_queryset(self):
        q = self.kwargs['username']
        if q != '*':
            return Subscriptions.objects.filter(username=q)
        else:
            return Subscriptions.objects.all()


def date_handler(obj):
    return obj.isoformat() if hasattr(obj, 'isoformat') else obj

