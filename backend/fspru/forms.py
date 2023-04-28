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


class RegistrationForm(ModelForm):
	class Meta:
		model = Users
		fields = ['first_name', 'second_name','login_email','status','phone','password']
		widgets = {
			'first_name' : TextInput(attrs = {
				'type' : 'text',
				'id' : 'form_first_name',
				'class' : 'form-control',
				'placeholder' : 'Имя'
				}),
			'second_name' : TextInput(attrs = {
				'type' : 'text',
				'id' : 'form_second_name',
				'class' : 'form-control',
				'placeholder' : 'Фамилия'
				}),
			'login_email' : TextInput(attrs = {
				'type' : 'text',
				'id' : 'form_login_email',
				'class' : 'form-control',
				'placeholder' : 'Логин'
				}),
			'status' : TextInput(attrs = {
				'type' : 'number',
				'id' : 'form_status',
				'class' : 'form-control'
				}),
			'phone' : TextInput(attrs = {
				'type' : 'text',
				'id' : 'form_phone',
				'class' : 'form-control',
				'placeholder' : 'form-control'
				}),
			'password' : TextInput(attrs = {
				'type' : 'password',
				'id' : 'form_password',
				'class' : 'form-control',
				'placeholder' : 'Пароль'
				})
		}
