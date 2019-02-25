from django.conf.urls import url

from . import views

urlpatterns = [
   url(r'^create/$', views.CategoryCreateView.as_view()),
   url(r'^list/$', views.CategoryListView.as_view()),
   url(r'^delete/(?P<pk>[^/]+)/$', views.CategoryRUDView.as_view()),
   url(r'', views.toi, name='toi'),

]