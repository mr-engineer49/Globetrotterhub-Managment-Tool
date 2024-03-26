from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.sessions.models import Session



from .forms import NewUserForm

# Create your views here.


def registration_view(request):
	if request.method == "POST":
		register_form = NewUserForm(request.POST)
		if register_form.is_valid():
			user = register_form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("dashboard:index")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	register_form = NewUserForm()
	request.session.set_test_cookie()
	return render (request=request, template_name="register.html", context={"register_form":register_form})






def login_view(request):
	if request.method == "POST":
		login_form = AuthenticationForm(request, data=request.POST)
		if login_form.is_valid():
			username = login_form.cleaned_data.get('username')
			password = login_form.cleaned_data.get('password')
			user = authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("dashboard:index")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	login_form = AuthenticationForm()
	request.session.set_test_cookie()
	return render(request=request, template_name="login.html", context={"login_form":login_form})




def logout_view(request):
	logout = Session.objects.all().delete()
	request.session.set_test_cookie()
	return render (request=request, template_name='homepage.html', context={
		'logout': logout
	})




