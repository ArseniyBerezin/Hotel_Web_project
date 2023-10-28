from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm

from users.models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-1', 'placeholder': 'Введите имя пользователя'
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control py-2', 'placeholder': 'Введите пароль'
    }))

    class Meta:
        model = User
        fields = ('username', 'password')


class UserRegistrationForm(UserCreationForm):
    class Meta:
        first_name = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control py-3', 'placeholder': 'Имя'
        }))
        last_name = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control py-3', 'placeholder': 'Фамилия'
        }))
        username = forms.CharField(widget=forms.TextInput(attrs={
            'class': 'form-control py-3', 'placeholder': 'Username'
        }))
        email = forms.CharField(widget=forms.EmailInput(attrs={
            'class': 'form-control py-3', 'placeholder': 'Email'
        }))
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control py-3', 'placeholder': 'Пароль'
        }))
        password2 = forms.CharField(widget=forms.PasswordInput(attrs={
            'class': 'form-control py-3', 'placeholder': 'Пароль'
        }))

        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3'
    }))
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control py-3', 'readonly': True
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'class': 'form-control py-3', 'readonly': True
    }))
    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file input'
    }), required=False)

    class Meta:
        model = User
        fields = ('image', 'first_name', 'last_name', 'username', 'email')
