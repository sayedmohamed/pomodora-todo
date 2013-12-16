from django import forms
import re
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):
	username=forms.CharField(label="Username",max_length=50)
	email=forms.EmailField(label='Email')
	password1=forms.CharField(label="password",widget=forms.PasswordInput())
	password2=forms.CharField(label="password (again)",widget=forms.PasswordInput())

	def clean_password2(self):
		if 'password2' in self.cleaned_data:
			password1=self.cleaned_data['password1']
			password2=self.cleaned_data['password2']
			if password1==password2:
				return password2
		else:
			raise forms.ValidationError('passwords do not match')


	def clean_username(self):
		username=self.cleaned_data['username']
		if not re.search(r'^\w+$', username):
			raise forms.ValidationError('username can contain only alphnumeric and characters')
		try:
			user=User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError('username already exist')