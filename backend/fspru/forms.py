from django.forms import ModelForm, TextInput
from .models import Users


class LoginForm(ModelForm):
	class Meta:
		model = Users
		fields = ['login_email', 'password']
		widgets = {'login_email': TextInput(attrs = {
				'type': 'email',
				'id': 'form_email',
				'class': 'form-control',
				'placeholder': 'email',
				}),
			'password': TextInput(attrs = {
				'type': 'password',
				'id': 'form_password',
				'class': 'form-control',
				'placeholder': 'пароль',
				}),
		}