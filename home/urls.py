from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . views import signup, home

urlpatterns = [
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^', home, name='home'),
    url(r'^signup/$', RegistrationView.as_view(), name='signup'),
    url(r'^signup/done/$', views.password_reset_done, {
        'template_name': 'signup_done.html',
    }, name='signup-done'),

    url(r'^signup/password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.password_reset_confirm, {
            'template_name': 'signup_confirm.html',
            'post_reset_redirect': 'home:signup-complete',
        }, name='signup-confirm'),
    url(r'^signup/complete/$', views.password_reset_complete, {
        'template_name': 'signup_complete.html',
    }, name='signup-complete'),
]