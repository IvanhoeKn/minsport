from django import forms
from .models import Users


class LoginForm(forms.ModelForm):
	class Meta:
		model = Users
		fields = ['login_email', 'password']