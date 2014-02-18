from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'com_fsw_service.views.index'),
                       # url(r'^fswproject_webservice/', include('fswproject_webservice.foo.urls')),

                       #Endpoints:
                       # User Authentication (Email & Password):
                       url(r'^new_user/$', 'com_fsw_service.views.new_user'),
                       url(r'^user_auth/$', 'com_fsw_service.views.user_auth'),
                       url(r'^logout/$','com_fsw_service.views.user_logout'),

                       #Setters:
                       # Allergies (Patient Id):
                       url(r'^set_allergies/$', 'com_fsw_service.views.allergies'),
                       # Diet (Patient Id):
                       url(r'^set_diet/$', 'com_fsw_service.views.diet'),
                       # Hospitalizations (Patient Id):
                       url(r'^set_hospitalizations/$', 'com_fsw_service.views.hospitalizations'),
                       # Medications (Patient Id):
                       url(r'^set_medications/$', 'com_fsw_service.views.medications'),
                       # Assessments (Patient Id):
                       url(r'^set_assessments/$', 'com_fsw_service.views.set_assessments'),
                       # Prescriptions (Patient Id):
                       url(r'^set_prescriptions/$', 'com_fsw_service.views.set_prescriptions'),
                       # Medication History (Patient Id):
                       url(r'^set_medication_history/$', 'com_fsw_service.views.medication_history'),
                       # Emergency_Contacts (Patient Id):
                       url(r'^set_emergency_contacts/$', 'com_fsw_service.views.emergency_contacts'),
                       # Notes (Patient Id):
                       url(r'^set_notes/$', 'com_fsw_service.views.notes'),
                       # Doctors (Patient Id):
                       url(r'^set_doctors/$', 'com_fsw_service.views.set_doctors'),
                       # Patients (Patient Id):
                       url(r'^set_patients/$', 'com_fsw_service.views.patients'),

                       #Getters:
                       # Allergies (Patient Id):
                       url(r'^get_allergies/$', 'com_fsw_service.views.allergies'),
                       # Diet (Patient Id):
                       url(r'^get_diet/$', 'com_fsw_service.views.diet'),
                       # Hospitalizations (Patient Id):
                       url(r'^get_hospitalizations/$', 'com_fsw_service.views.hospitalizations'),
                       # Medications (Patient Id):
                       url(r'^get_medications/$', 'com_fsw_service.views.medications'),
                       # Assessments (Patient Id):
                       url(r'^get_assessments/$', 'com_fsw_service.views.assessments'),
                       # Prescriptions (Patient Id):
                       url(r'^get_prescriptions/$', 'com_fsw_service.views.prescriptions'),
                       # Medication History (Patient Id):
                       url(r'^get_medication_history/$', 'com_fsw_service.views.medication_history'),
                       # Emergency_Contacts (Patient Id):
                       url(r'^get_emergency_contacts/$', 'com_fsw_service.views.emergency_contacts'),
                       # Notes (Patient Id):
                       url(r'^get_notes/$', 'com_fsw_service.views.notes'),
                       # Doctors (Patient Id):
                       url(r'^get_doctors/$', 'com_fsw_service.views.doctors'),
                       # Patients (Patient Id):
                       url(r'^get_patients/$', 'com_fsw_service.views.patients'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
)
