from django import forms 
from django.contrib.auth.models import User

def must_be_gt(value_password):
	if len(value_password) < 5:
		raise forms.ValidationError('El password debe tener mas de 5 caracteres')

class LoginForm(forms.Form):
	username = forms.CharField(max_length = 30, required = True)
	password = forms.CharField(max_length = 30, widget = forms.PasswordInput())

	def __init__(self, *args, **kwargs):
		super(LoginForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update( {'placeholder' : 'Usuario' } )
		self.fields['password'].widget.attrs.update( {'placeholder' : 'Contraseña' } )

class RegisterForm(forms.ModelForm):
	username = forms.CharField(max_length = 20, required = True)
	password = forms.CharField(max_length = 20, required = True, widget = forms.PasswordInput(),  validators = [must_be_gt])
	email = forms.CharField(required = True)

	def __init__(self, *args, **kwargs):
		super(RegisterForm, self).__init__(*args, **kwargs)
		self.fields['username'].widget.attrs.update( {'placeholder' : 'Usuario' } )
		self.fields['password'].widget.attrs.update( {'placeholder' : 'Contraseña' } )
		self.fields['email'].widget.attrs.update({'placeholder' : 'Email' } )

	def clean_email(self):
		email = self.cleaned_data.get('email')
		if User.objects.filter(email=email).count():
			raise forms.ValidationError('El email ya existe')
		return email

	class Meta:
		model = User
		fields = ("username", "email", "password")


