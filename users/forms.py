from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegForm(UserCreationForm):
    email = forms.EmailField(
        label='Введите Email',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите Email'})
    )
    username = forms.CharField(
        label='Введите логин',
        required=True,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите логин'})
    )
    password1 = forms.CharField(
        label='Введите пароль',
        required=True,
        help_text='Пароль не должен быть слишком легким',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Введите пароль'})
    )
    password2 = forms.CharField(
        label='Подтвердите пароль',
        required=True,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Подтвердите пароль'})
    )

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'email']
