# mysite/urls.py

from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()


from meetingroom.views import hello_world, members, menu

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello_world),
    url(r'^menu/$', members),
    url(r'^members/$', members),
)