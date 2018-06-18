from django.conf.urls import url
from organizer.views import NewslinkCreate, NewslinkUpdate, NewslinkDelete

app_name='organizer_newslink'

urlpatterns = [
    url(r'^create/$', NewslinkCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/update/$', NewslinkUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', NewslinkDelete.as_view(), name='delete')
]
