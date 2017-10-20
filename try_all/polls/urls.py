from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.poll_index, name='poll_index'),
    url(r'^(?P<question_id>\d+)/$', views.poll_detail, name='poll_detail'),
    url(r'^(?P<question_id>\d+)/vote/$', views.poll_vote, name='poll_vote'),
    url(r'^(?P<question_id>\d+)/result/$', views.poll_result, name='poll_result'),
]
