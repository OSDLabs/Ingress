from django.conf.urls import include, url
from django.contrib import admin	

urlpatterns = [
    url(r'^$', 'user.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^infographics/', include('infographics.urls')),
    url(r'^cab/', include('cab.urls'))
]
