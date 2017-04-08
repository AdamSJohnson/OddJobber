from django.shortcuts import render
from . forms import UserForm, UserProfileForm
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def signup(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix = 'user')
        upf = UserProfileForm(request.POST, prefix = 'userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit = False)
            userprofile.user = user
            userprofile.save()
            return HttpResponseRedirect('/home/')

    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix = 'userprofile')
    return render_to_response('signup.html',
                               dict(userform = uf, userprofileform = upf))

