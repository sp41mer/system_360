from django import forms
from django.contrib.auth.forms import UserCreationForm

from core.models import User


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'patronymic_name', 'last_name', 'department', 'password1', 'password2']


class ChangeUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
