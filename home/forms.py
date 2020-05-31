from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SearchForm(forms.Form):
    query = forms.CharField(label='Arama', max_length=100)

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=100, label='Kullanıcı Adı')
    first_name = forms.CharField(max_length=100, label='Ad')
    last_name = forms.CharField(max_length=100, label='Soyad')
    email = forms.EmailField(max_length=200, label='Email')

    class Meta:
        model = User
        fields = {'username', 'email', 'first_name', 'last_name', 'password1', 'password2'}