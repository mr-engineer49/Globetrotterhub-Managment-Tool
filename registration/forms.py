from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



# Create your forms here.

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)
	username = forms.CharField(label='Username', max_length=100, required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		user.username = self.cleaned_data['username']
		user.password1 = self.cleaned_data['password1']
		if commit:
			user.save()
		return user