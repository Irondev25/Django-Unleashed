from django.conf.urls import url
from organizer.views import StartupList, StartupCreate, StartupDetail, StartupUpdate, StartupDelete

app_name = 'organizer_startup'


urlpatterns=[
    url(r'^$', StartupList.as_view(), name='list'),
    url(r'^create/$', StartupCreate.as_view(), name='create'),
    url(r'^(?P<slug>[\w\-]+)/$', StartupDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[\w\-]+)/update/$', StartupUpdate.as_view(), name='update'),
    url(r'^(?P<slug>[\w\-]+)/delete/$', StartupDelete.as_view(), name='delete'),
]
