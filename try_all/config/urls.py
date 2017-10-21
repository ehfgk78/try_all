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
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

from blog.views import post_list, post_detail, post_add, post_delete
from config import settings
from config.views import index
from polls.views import poll_index, poll_detail, poll_vote, poll_result

urlpatterns = [
    ### admin ###
    url(r'^admin/', admin.site.urls),
    url(r'^$', index),
    ### blog ###
    url(r'^blog/', include('blog.urls', namespace='blog')),
    ### polls ###
    url(r'^polls/', include('polls.urls', namespace='polls')),
    ### models_doc ###
    url(r'^models/', include('models_doc.urls', namespace='models')),
    ### instagram ###
    url(r'^instagram/', include('instagram.urls', namespace='instagram')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT,
)
