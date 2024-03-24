from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# Create your forms here.

REGISTER_CLASS = "w-96 bg-gray-200 mx-auto outline rounded-lg shadow-xl"
PASSWORD_CLASS = "form-text bg-yellow-100 border border-yellow-400 text-yellow-700 px-4 py-3 rounded relative"


class NewUserForm(UserCreationForm):
	email = forms.EmailField(label='Email', required=True)
	username = forms.CharField(label='Username', max_length=100, required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")
		widgets={
			'username': forms.TextInput(attrs={
			'placeholder':  'Enter username...', 
			'class': f'{REGISTER_CLASS}border rounded w-96 bg-gray-200 mx-auto py-2 px-3 text-gray-700 leading-tight focus:outline focus:shadow-outline',
			'id': 'username'
			}),
			'email': forms.EmailInput(attrs={
			'placeholder':  'Enter email...',
			'class': f'{REGISTER_CLASS} appearance-none border rounded w-96 bg-gray-200 mx-auto py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
			}),
			'password1': forms.EmailInput(attrs={
			'placeholder':  'Enter password...',
			'class': f'{REGISTER_CLASS} appearance-none border rounded w-96 bg-gray-200 mx-auto py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
			'id': 'id_password1_helptext'
			}),
			'password2': forms.EmailInput(attrs={
			'placeholder':  'Enter again same password...',
			'class': f'{REGISTER_CLASS} appearance-none border rounded w-96 bg-gray-200 mx-auto py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline',
			}),
		}

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['username']
		user.password1 = self.cleaned_data['password1']
		if commit:
			user.save()
		return user