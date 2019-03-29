from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'news', views.toi, name='toi'),

   url(r'^videos/$', views.videos, name='videos'),
   url(r'^city/$', views.city, name='city'),
   url(r'^india/$', views.india, name='india'),
   url(r'^elections/$', views.elections, name='elections'),
   url(r'^world/$', views.world, name='world'),
   url(r'^business/$', views.business, name='business'),
   url(r'^tech/$', views.tech, name='tech'),
   url(r'^cricket/$', views.cricket, name='cricket'),
   url(r'^sports/$', views.sports, name='sports'),
   url(r'^entertainment/$', views.entertainment, name='entertainment'),
   url(r'^web-series/$', views.web_series, name='web-series'),
   url(r'^life-style/$', views.life_style, name='life-style'),
   url(r'^blogs/$', views.blogs, name='blogs'),
   url(r'^photos/$', views.photos, name='photos'),
   url(r'^live-tv/$', views.live_tv, name='live-tv'),
   url(r'^education/$', views.education, name='education'),
   url(r'^all-sections/$', views.all_sections, name='all-sections'),

   # url(r'base/$', views.base, name='base'),  #example for django forms


   url(r'^l1/create/$', views.Level1CreateView.as_view()),
   url(r'^l1/list/$', views.Level1ListView.as_view()),
   url(r'^l1/delete/(?P<pk>[^/]+)/$', views.Level1RUDView.as_view()),

   url(r'^l2/create/$', views.Level2CreateView.as_view()),
   url(r'^l2/list/$', views.Level2ListView.as_view()),
   url(r'^l2/delete/(?P<pk>[^/]+)/$', views.Level2RUDView.as_view()),

   url(r'^l3/create/$', views.Level3CreateView.as_view()),
   url(r'^l3/list/$', views.Level3ListView.as_view()),
   url(r'^l3/delete/(?P<pk>[^/]+)/$', views.Level3RUDView.as_view()),

]