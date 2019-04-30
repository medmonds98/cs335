"""mysite URL Configuration

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
from polls import views as polls_views

admin.autodiscover()

urlpatterns = [
    url(r'^$', polls_views.index),
    url(r'^polls/$',polls_views.index),
    url(r'^polls/newpoll/$', polls_views.getPoll),
    url(r'^polls/results$', polls_views.full_results),
    url(r'^polls/(?P<poll_id>\d+)/results/$', polls_views.results),
    url(r'^polls/(?P<poll_id>\d+)/$', polls_views.vote),
    url(r'^admin/',admin.site.urls),
]
