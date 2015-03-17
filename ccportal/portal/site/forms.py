from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from models import User

class UserCreationForm(UserCreationForm):
    """
    A form that creates a user, with no privileges, from the given email and
    password.
    """

    def __init__(self, *args, **kargs):
        super(UserCreationForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = User
        fields = ["email",]

class UserChangeForm(UserChangeForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """

    def __init__(self, *args, **kargs):
        super(UserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
        model = User
        fields = []


class LoginForm(forms.Form):
    email = forms.CharField(max_length=254, widget=forms.TextInput(attrs={'placeholder': 'Email Address'}))
    password = forms.CharField(max_length=254, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))