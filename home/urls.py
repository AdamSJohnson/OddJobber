from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . views import signup, home

urlpatterns = [
    url(r'^signup/', signup, name='signup'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^', home, name='home'),
]