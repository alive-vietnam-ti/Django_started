from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20)
    email = forms.EmailField()
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)


class LoginForm(forms.Form):
    emailOrUsername = forms.CharField(max_length=100)
    password = forms.CharField(max_length=20, widget=forms.PasswordInput)
