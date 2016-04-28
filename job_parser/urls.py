from django.conf.urls import url
from views import job_post, content

urlpatterns = [
    url(r'^$', job_post.index, name='index'),
    url(r'^(?P<job_post_id>[0-9]+)/$', job_post.show, name='show'),
    url(r'^(?P<job_post_id>[0-9]+)/edit$', job_post.edit, name='edit'),
    url(r'^content/(?P<content_id>[0-9]+)$', content.single, name='single'),
    url(r'^content/(?P<content_id>[0-9]+)/edit$', content.edit, name='content_edit'),
]