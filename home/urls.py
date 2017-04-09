from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . views import signup, home, myprofile, logout_view, edit_profile

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),

    url(r'^signup/', signup.as_view(), name='signup'),

    url(r'^profile/edit/', edit_profile.as_view(), name='edit_profile'),

    url(r'^profile/', myprofile.as_view(), name='profile'),

    url(r'^logout/', logout_view, name='logout'),

    url(r'^', signup.as_view(), name='home'),
]