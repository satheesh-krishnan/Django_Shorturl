from django.conf.urls import url

from surl import views

urlpatterns=[
             url(r'^home/$', views.home),
             url(r'^(?P<uname>\w+)/$',views.newu),
            ]
