from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from django.views.generic import CreateView

from . forms import UserCreationForm


class signup(CreateView):
    template_name = 'signup_create.html'
    form_class = UserCreationForm
    success_url = '/home/'



def home(request):
    return render(
        request,
        'home.html',
    )
