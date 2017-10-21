from django.conf.urls import url

from instagram import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^create/$', views.post_create, name='post_create'),
    url(r'(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^create/comment/(?P<post_id>\d+)/$',
        views.comment_create, name='comment_create'),
]
