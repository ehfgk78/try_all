"""try_all URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from blog.views import post_list, post_detail, post_add, post_delete
from polls.views import poll_index

urlpatterns = [
    ### blog ###
    url(r'^admin/', admin.site.urls),
    url(r'^$', post_list, name='post_list'),
    # post_id <== 장고템플릿 : name으로  views.post_detail을 인식함
    # post <-- context <-- posts <-- views.post_list <== models.Post
    url(r'^posts/(?P<post_id>\d+)/$', post_detail, name='post_detail'),
    url(r'^posts/add/$', post_add, name='post_add'),
    url(r'^posts/(?P<post_id>\d+)/delete/$', post_delete, name='post_delete'),

    ### polls ###
    url(r'^polls/$', poll_index, name='poll_index'),
    # url(r'^polls/(?P<question_id>\d+)/$', poll_detail, name='poll_detail'),
    # url(r'^polls/(?P<question_id>\d+)/result/$', poll_result, name='poll_result'),
    # url(r'^polls/(?P<question_id>\d+)/vote/$', poll_vote, name='poll_vote'),
]










