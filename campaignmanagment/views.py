from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import  render, redirect
from .forms import NewCampaignForm
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import  login_required

# Create your views here.
@login_required()
def campaigns_view(request):
    new_campaign = NewCampaignForm()
    return render(request, 'campaigns.html', context={
        'new_campaign':new_campaign
    })



@login_required()
def new_campaign(request):
    if request.method == "POST":
        new_campaign = NewCampaignForm(request.POST, request.FILES)
        if new_campaign.is_valid():
            new_campaign.save()

            return redirect("campaignmanagment:campaigns_form")
        else:
            new_campaign = NewCampaignForm()
    return render (request=request, template_name="campaigns.html", context={"new_campaign":new_campaign})
