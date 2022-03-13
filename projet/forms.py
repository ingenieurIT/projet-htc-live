from django.contrib.auth import forms
from django.db.models import fields
from django.db.models.base import Model
from django.forms import ModelForm
from django import forms
from .models import Ordinateur
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class OrdiForm(ModelForm):
    class Meta:
        model = Ordinateur
        fields = '__all__'
        exclude = ['createur', 'likesO']
        

class CreerUtilisateur(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        

class AdminLoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
