from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label ='Логин',
        required=True
    )
    password = forms.CharField(
        label='Пароль',
        required=True,
        widget=forms.PasswordInput)