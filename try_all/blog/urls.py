from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',  views.post_list, name='post_list'),
    url(r'^(?P<post_id>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^add/$', views.post_add, name='post_add'),
    url(r'^(?P<post_id>\d+)/delete/$', views.post_delete,
        name='post_delete'
        ),
]