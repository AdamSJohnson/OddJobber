from django.forms import ModelForm
from django import forms
from . models import User

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'email', 'first_name', 'last_name', 'phone', 'street', 'city', 'state', 'zipcode']


class UserCreationForm ( ModelForm ) :

    password1 = forms.CharField( label = 'Password', widget = forms.PasswordInput )
    password2 = forms.CharField( label = 'Password confirmation', widget = forms.PasswordInput )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone', 'street', 'city', 'state', 'zipcode')

    def clean_password2 ( self ) :
        # Check that the two password entries match
        password1 = self.cleaned_data.get( "password1" )
        password2 = self.cleaned_data.get( "password2" )
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError( "Passwords don't match" )
        return password1

    def save( self, commit = True ) :
        # Save the provided password in hashed format
        user = super( UserCreationForm, self ).save( commit = False )
        user.set_password( self.cleaned_data[ "password1" ] )
        if commit:
            user.save()
        return user
