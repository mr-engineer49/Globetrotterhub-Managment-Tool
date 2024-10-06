from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from django.contrib import messages


# Create your views here.

@login_required
def index_client(request):
    if request.user.is_authenticated:

        return render(request, 'dashboard.html', context={
        
    })


@login_required
def index_client_form(request):
    if request.user.is_authenticated:
        messages.info(request, "You are now logged in.")
        return render(request, 'dashboard.html', context={

        })



@login_required
def profile_view(request):
    user_name = request.user.username
    user_email = request.user.email
    user_password = request.user.password

    return render (request, 'profile.html', context={
        'user_name':user_name,
        'user_email':user_email,
        'user_password':user_password
    })
