from django.conf.urls import url
from organizer.views import (TagList, TagPageList, TagCreate, 
                             TagDetail, TagUpdate, TagDelete)

app_name = 'organizer_tag'

urlpatterns = [
    url(r'^$', TagList.as_view(), name='list'),
    url(r'^(?P<page_number>\d+)/$', TagPageList.as_view(), name='page'),
    url(r'^create/$', TagCreate.as_view(), name='create'),
    #using Detail view directly passing parameters in as_view()
    # url(r'^(?P<slug>[-\w]+)/$', DetailView.as_view(
    #     model = Tag,
    #     context_object_name = 'tag',
    #     template_name='organizer/tag_detail.html'
    # ), name='detail'),
    url(r'^(?P<slug>[-\w]+)/$', TagDetail.as_view(), name='detail'),
    url(r'^(?P<slug>[-\w]+)/update/$', TagUpdate.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/delete/$', TagDelete.as_view(), name='delete'),
]
