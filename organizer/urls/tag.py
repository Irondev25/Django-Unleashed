from django.conf.urls import url
from organizer.views import tag_list, TagCreate, tag_detail, TagUpdate, TagDelete

app_name = 'organizer_tag'

urlpatterns = [
    url(r'^$', tag_list, name='list'),
    url(r'^create/$', TagCreate.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', tag_detail, name='detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', TagUpdate.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', TagDelete.as_view(), name='delete'),
]
