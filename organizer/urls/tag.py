from django.conf.urls import url
from organizer.views import (TagList, TagPageList, TagCreate, 
                             tag_detail, TagUpdate, TagDelete)

app_name = 'organizer_tag'

urlpatterns = [
    url(r'^$', TagList.as_view(), name='list'),
    url(r'^(?P<page_number>\d+)/$', TagPageList.as_view(), name='page'),
    url(r'^create/$', TagCreate.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', tag_detail, name='detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', TagUpdate.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', TagDelete.as_view(), name='delete'),
]
