from django.conf.urls import url
from organizer.views import startup_list, StartupCreate, startup_detail, StartupUpdate, StartupDelete

app_name = 'organizer_startup'


urlpatterns=[
    url(r'^$', startup_list, name='list'),
    url(r'^create/$', StartupCreate.as_view(), name='create'),
    url(r'^(?P<slug>[\w\-]+)/$', startup_detail, name='detail'),
    url(r'^(?P<slug>[\w\-]+)/update/$', StartupUpdate.as_view(), name='update'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', StartupDelete.as_view(), name='delete'),
]