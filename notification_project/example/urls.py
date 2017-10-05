from django.conf.urls import url
from example.views import *

app_name = 'example'

urlpatterns = [
    url(r'^critical/$', critical, name="critical"),
    url(r'^error/$', error, name="error"),
    url(r'^other/$', others, name="nuevo"),
    url(r'^userloggedcritical/$', userloggedcritical, name="critical_1"),
    url(r'^userloggederror/$', userloggederror, name="error_1"),
    url(r'^uncaught/$', uncaught, name="uncaught"),
]
