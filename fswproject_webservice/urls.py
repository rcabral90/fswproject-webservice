from django.conf.urls import patterns, include, url
from django.views.generic import RedirectView
from rest_framework.urlpatterns import format_suffix_patterns
from com_fsw_service import views
from rest_framework import routers
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.db.models.loading import cache as model_cache

if not model_cache.loaded:
    model_cache.get_models()

admin.autodiscover()

urlpatterns = format_suffix_patterns(patterns('',

                                              url(r'^$', 'com_fsw_service.views.api_root'),

                                              url(r'^api-auth/',
                                                  include('rest_framework.urls', namespace='rest_framework')),

                                              url(r'^diets/(?P<resident_id>.+)/$', views.DietViewSet.as_view(),
                                                  name='diets-details'),

                                              # User Authentication (Email & Password):

                                              url(r'^new_user/$', 'com_fsw_service.views.new_user',
                                                  name='new user'),

                                              url(r'^user_auth/$', 'com_fsw_service.views.user_auth',
                                                  name='user login'),

                                              url(r'^logout/$', 'com_fsw_service.views.user_logout',
                                                  name='user logout'),


                                              # Uncomment the admin/doc line below to enable admin documentation:
                                              url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                                              # Uncomment the next line to enable the admin:
                                              url(r'^admin/', include(admin.site.urls)),
))

urlpatterns += patterns('',
                        url(r'^api-auth/', include('rest_framework.urls',
                                                   namespace='rest_framework')),
)

