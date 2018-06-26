from django.conf.urls import url
from . import views           
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^viewpostedby/(?P<id>\d+)$', views.viewpostedby),
    url(r'^editmyaccountpage/(?P<id>\d+)$', views.editmyaccountpage),
    url(r'^deletequote/(?P<id>\d+)$', views.deletequote),
    url(r'^dashboard$', views.dashboard),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^addquote$', views.addquote),
    url(r'^editaccount$', views.editaccount),
    url(r'^like$', views.like),
    

]