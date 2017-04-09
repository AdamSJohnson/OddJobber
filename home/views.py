from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from django.contrib.auth.forms import PasswordResetForm
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView, UpdateView

from . forms import UserCreationForm, UserForm
from django.urls import reverse_lazy


from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from . models import User
from django.forms.models import inlineformset_factory
from django.core.exceptions import PermissionDenied

class signup(CreateView):
    template_name = 'signup_create.html'
    form_class = UserCreationForm
    success_url = '/home/'

def home(request):
    return render(
        request,
        'home.html',
    )

#@login_required() # only logged in users should access this
class myprofile(DetailView):
    model = User
    template_name = 'profile_owner.html'
    success_url = '/home/'

    def get_object(self):
        print(self.request.user)
        return self.request.user

#@login_required()
class edit_profile(UpdateView):
    model = User
    fields = ['avatar', 'first_name', 'last_name', 'phone', 'street', 'city', 'state', 'zipcode']
    template_name = 'profile_edit.html'
    form = UserForm
    success_url = reverse_lazy('profile')


    def get_object(self):
        print(self.request.user)
        return self.request.user

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse_lazy('home'))
