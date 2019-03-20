from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'', views.toi, name='toi'),

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