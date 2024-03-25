from django.shortcuts import  render, redirect
from django.contrib.auth import login
from django.contrib import messages
from django.shortcuts import  render, redirect
from .forms import NewCampaignForm
from .models import NewCampaignModel
from django.contrib.auth import login, authenticate, logout #add this
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this
from django.contrib.sessions.models import Session
from django.contrib.auth.decorators import  login_required

# Create your views here.
@login_required()
def campaigns_view(request):
    new_campaign = NewCampaignModel.objects.filter(is_active=True)
    return render(request, 'campaigns.html', context={
        'new_campaign':new_campaign,
    })



@login_required()
def new_campaign(request):
    if request.method == "POST":
        new_campaign_form = NewCampaignForm(request.POST)
        if new_campaign_form.is_valid():
            new_campaign_form.save()
            print("new campaign created!")
            return redirect("campaignmanagment:campaigns_form")
        else:
            print(f"Error creating new campaign !!! {new_campaign_form.errors}")
    else:
        new_campaign_form = NewCampaignForm()

    return render (request, "campaigns.html", context={
        "new_campaign_form":new_campaign_form,
        })
