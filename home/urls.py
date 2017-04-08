from django.conf.urls import url, include
from django.contrib import admin
from . views import signup

urlpatterns = [
    #url(r'^home/', include('OddJobber.home.urls')),
    url(r'^signup/', signup),
]