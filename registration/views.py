from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

from .forms import NewUserForm

# Create your views here.


def registration(request):
	if request.method == "POST":
		register_form = NewUserForm(request.POST)
		if register_form.is_valid():
			user = register_form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("main:homepage")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	register_form = NewUserForm()
	return render (request=request, template_name="register.html", context={"register_form":register_form})






def login(request):
	if request.method == "POST":
		login_form = AuthenticationForm(request, data=request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data.get('username')
			password = login_form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	login_form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":login_form})







