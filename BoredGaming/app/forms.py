"""
Definition of forms.
"""

from django import forms
from django.forms.fields import EmailField
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

class BootstrapAuthenticationForm(AuthenticationForm):
    """Authentication form which uses boostrap CSS."""
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'User name'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Password'}))

class MailingListForm(forms.Form):
   """Mailing list """
   email = forms.EmailField(required=True)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        widgets = {
            'username':forms.TextInput(attrs =
                                       {
                                           'class':'form-control',
                                           'placeholder':'Username'
                                        }), 
            'first_name':forms.TextInput(attrs =
                                       {
                                           'class':'form-control',
                                           'placeholder':'First Name'
                                        }),
            'last_name':forms.TextInput(attrs =
                                       {
                                           'class':'form-control',
                                           'placeholder':'Last Name'
                                        }),
            'email':forms.EmailInput(attrs =
                                       {
                                           'class':'form-control',
                                           'placeholder':'Email - required'
                                        }),
            'password1':forms.PasswordInput(attrs =
                                       {
                                           'class':'form-control',
                                           'placeholder':'Password'
                                        }),
            'password2':forms.PasswordInput(attrs =
                                       {
                                           'class':'form-control',
                                           'placeholder':'Confirm Password'
                                        })
            }
