from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import SupportRequest

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
class SupportRequestForm(forms.ModelForm):
    class Meta:
        model = SupportRequest
        fields = ['subject', 'description']
        widgets = {
            'subject': forms.TextInput(attrs={
                'placeholder': 'Muammo mavzusi',
                'class': 'form-control'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Muammo haqida batafsil yozing',
                'class': 'form-control',
                'rows': 4
            }),
        }
