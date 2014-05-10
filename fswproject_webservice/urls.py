from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from com_fsw_service import views
from django.contrib import admin
from django.db.models.loading import cache as model_cache

if not model_cache.loaded:
    model_cache.get_models()

admin.autodiscover()

urlpatterns = format_suffix_patterns(patterns('',

                                              url(r'^$', 'com_fsw_service.views.api_root'),

                                              url(r'^api-auth/',
                                                  include('rest_framework.urls', namespace='rest_framework')),

                                              # User Authentication (Email & Password):

                                              url(r'^new_user/$', 'com_fsw_service.views.new_user',
                                                  name='new user'),

                                              url(r'^user_auth/$', 'com_fsw_service.views.user_auth',
                                                  name='user login'),

                                              url(r'^current_user/$', 'com_fsw_service.views.current_user',
                                                  name='current user'),

                                              url(r'^logout/$', 'com_fsw_service.views.user_logout',
                                                  name='user logout'),

                                              url(r'^diets/(?P<resident_id>.+)/$', views.DietViewSet.as_view(),
                                                  name='diets-details'),

                                              url(r'^allergies/(?P<resident_id>.+)/$', views.AllergiesViewSet.as_view(),
                                                  name='allergies-details'),

                                              url(r'^hospitalization/(?P<resident_id>.+)/$',
                                                  views.HospitalizationsViewSet.as_view(),
                                                  name='hospitalization-details'),

                                              url(r'^medication/(?P<resident_id>.+)/$',
                                                  views.MedicationsViewSet.as_view(),
                                                  name='medication-details'),

                                              url(r'^assessment/(?P<resident_id>.+)/$',
                                                  views.AssessmentsViewSet.as_view(),
                                                  name='assessment-details'),

                                              url(r'^prescription/(?P<resident_id>.+)/$',
                                                  views.PrescriptionsViewSet.as_view(),
                                                  name='prescription-details'),

                                              url(r'^medicationhistory/(?P<resident_id>.+)/$',
                                                  views.MedicationHistoryViewSet.as_view(),
                                                  name='medicationhistory-details'),

                                              url(r'^emergencycontacts/(?P<resident_id>.+)/$',
                                                  views.EmergencyContactsViewSet.as_view(),
                                                  name='emergencycontacts-details'),

                                              url(r'^notes/(?P<resident_id>.+)/$', views.NotesViewSet.as_view(),
                                                  name='notes-details'),

                                              url(r'^doctors/(?P<doctor_id>.+)/$', views.DoctorsViewSet.as_view(),
                                                  name='doctors-details'),

                                              url(r'^residents/(?P<resident_id>.+)/$', views.ResidentViewSet.as_view(),
                                                  name='residents-details'),

                                              url(r'^residentstodoctor/(?P<resident_id>.+)/$',
                                                  views.ResidentToDoctorViewSet.as_view(),
                                                  name='residents-to-doctor-details'),

                                              url(r'^physical/(?P<resident_id>.+)/$',
                                                  views.PhysicalViewSet.as_view(),
                                                  name='physical-details'),

                                              url(r'^insurance/(?P<resident_id>.+)/$',
                                                  views.InsuranceViewSet.as_view(),
                                                  name='insurance-details'),

                                              url(r'^documents/(?P<resident_id>.+)/$',
                                                  views.DocumentStorageViewSet.as_view(),
                                                  name='document-details'),

                                              url(r'^alerts/(?P<resident_id>.+)/$',
                                                  views.AlertsViewSet.as_view(),
                                                  name='alert-details'),

                                              url(r'^subscriptions/(?P<username>.+)/$',
                                                  views.SubscriptionViewSet.as_view(),
                                                  name='subscriptions-details'),

                                              # Uncomment the admin/doc line below to enable admin documentation:
                                              url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                                              # Uncomment the next line to enable the admin:
                                              url(r'^admin/', include(admin.site.urls)),
))

urlpatterns += patterns('',
                        url(r'^api-auth/', include('rest_framework.urls',
                                                   namespace='rest_framework')),
)

