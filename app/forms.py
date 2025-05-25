from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Foydalanuvchi nomi'}),
            'email': forms.EmailInput(attrs={'class': 'input', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Parol'}),
            'password2': forms.PasswordInput(attrs={'class': 'input', 'placeholder': 'Parolni tasdiqlang'}),
        }
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }
