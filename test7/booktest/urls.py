from django.conf.urls import url

from booktest import views

urlpatterns = [
    url(r'^setsession$', views.setsession),
    url(r'^getsession$', views.getsession),
]
