"""djangomp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views

from django.conf.urls import url
# from django.urls import path

from . import views

urlpatterns = [
	url(r'^$', views.post_list, name='post_list'),  # see views.py in blog folder
	url(r'^home/$', views.post_list, name='post_list'),
	url(r'^login/$', auth_views.login, name='login'),
	url(r'^logout/$', auth_views.logout, {'next_page': '/home/'}, name='logout'),
	url(r'^signup/$', views.signup, name='signup'),
	url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
	url(r'^post/5/$', views.post_detail_audience_reactions, name='post_detail_audience_reactions'),
	url(r'^post/6/$', views.post_detail_choosing_keywords, name='post_detail_choosing_keywords'),
	url(r'^post/7/$', views.post_detail_choosing_topics, name='post_detail_choosing_topics'),
	url(r'^post/7//ca/$', views.post_detail_choosing_topics, name='post_detail_choosing_topics_ca'),
	url(r'^post/7//de/$', views.post_detail_choosing_topics_de, name='post_detail_choosing_topics_de'),
	url(r'^post/7//fr/$', views.post_detail_choosing_topics_fr, name='post_detail_choosing_topics_fr'),
	url(r'^post/7//gb/$', views.post_detail_choosing_topics_gb, name='post_detail_choosing_topics_gb'),
	url(r'^post/7//us/$', views.post_detail_choosing_topics_us, name='post_detail_choosing_topics_us'),
	url(r'^post/7/(?P<pk_letter>[\w|\W]+)/$', views.post_detail_choosing_topics_search, name='post_detail_choosing_topics_search'),
	url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'), # '\d+' = only digits -> value saved to pk
	url(r'^post/new/$', views.post_new, name='post_new'),
	url(r'^graphEnthusiasm/$', views.graphEnthusiasm, name='graphEnthusiasm'),
]
