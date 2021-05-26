from django import forms

from inputdata.models import Account
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    phone = forms.CharField(max_length=11, help_text='Introduzca su númeto de teléfono')

    class Meta:
        model = Account
        fields = ['username', 'password1', 'password2', 'personal_id']