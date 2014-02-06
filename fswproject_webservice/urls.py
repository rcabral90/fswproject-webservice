from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'com_fsw_service.views.index'),
                       # url(r'^fswproject_webservice/', include('fswproject_webservice.foo.urls')),

                       #Endpoints
                       # User Authentication (Email & Password):
                       url(r'^user_auth/$', 'com_fsw_service.views.user_auth'),
                       # Allergies (Patient Id):
                       url(r'^allergies/$', 'com_fsw_service.views.allergies'),
                       # Diet (Patient Id):
                       url(r'^diet/$', 'com_fsw_service.views.diet'),
                       # Hospitalizations (Patient Id):
                       url(r'^hospitalizations/$', 'com_fsw_service.views.hospitalizations'),
                       # Medications (Patient Id):
                       url(r'^medications/$', 'com_fsw_service.views.medications'),
                       # Assessments (Patient Id):
                       url(r'^assessments/$', 'com_fsw_service.views.assessments'),
                       # Prescriptions (Patient Id):
                       url(r'^prescriptions/$', 'com_fsw_service.views.prescriptions'),
                       # Medication History (Patient Id):
                       url(r'^medication_history/$', 'com_fsw_service.views.medication_history'),
                       # Emergency_Contacts (Patient Id):
                       url(r'^emergency_contacts/$', 'com_fsw_service.views.emergency_contacts'),
                       # Notes (Patient Id):
                       url(r'^notes/$', 'com_fsw_service.views.notes'),
                       # Doctors (Patient Id):
                       url(r'^doctors/$', 'com_fsw_service.views.doctors'),
                       # Patients (Patient Id):
                       url(r'^patients/$', 'com_fsw_service.views.patients'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
)
