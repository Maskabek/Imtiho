from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from todoapp.models import Todo


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']


class LoginForm(AuthenticationForm):
    class Meta:
        model = User


class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = ('text', 'expires_at', 'owner')
