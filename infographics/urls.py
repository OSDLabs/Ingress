from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'infographics.views.timetable', name='timetable'),
    url(r'^setup/$', 'infographics.views.setup', name = 'setup'),
]
