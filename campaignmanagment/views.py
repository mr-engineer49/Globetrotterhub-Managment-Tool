from django.shortcuts import  render, redirect, get_object_or_404
from .forms import NewCampaignForm, EditCampaignForm
from .models import NewCampaignModel
from django.contrib.auth.decorators import  login_required
import random
import time
from django.contrib import messages



# Create your views here.
@login_required
def campaigns_view(request):
    campaigns = NewCampaignModel.objects.filter(published_by=request.user)
    random_clicks = random.randint(100000, 999999)
    random_impressions = random.randint(100000, 999999)
    messages.info(request, "This is the Page of the Campaign Managment")
    NewCampaignModel.objects.filter(published_by=request.user, is_pending=True)
    campaigns.update(is_pending=False, is_active=True)



    return render(request, 'campaigns.html', context={
        'random_clicks': random_clicks,
        'random_impressions': random_impressions,
        'campaigns':campaigns,
    })



@login_required
def new_campaign_view(request):
    if request.method == "POST":
        campaign_form = NewCampaignForm(request.POST, request.FILES)
        
        if campaign_form.is_valid():
            campaign = campaign_form.save(commit=False)
            campaign.published_by = request.user
            campaign.save()
            print("new campaign created!")
            messages.success(request, "The New Document is Created !")


            return redirect("campaignmanagment:campaign_detail", pk=campaign.id)
        else:
            print(f"Error creating new campaign !!! {campaign_form.errors}")
            messages.error(request, "Error occured while tried to create new document !")
    else:
        campaign_form = NewCampaignForm()

    return render (request, "forms.html", context={
        "campaign_form":campaign_form,
        'title': 'New Campaign'
        })




@login_required
def edit_campaign_view(request, pk):
    campaign = get_object_or_404(NewCampaignModel, pk=pk, published_by=request.user)

    if request.method == 'POST':
        campaign_form = EditCampaignForm(request.POST, request.FILES, instance=campaign)

        if campaign_form.is_valid():
            campaign = campaign_form.save(commit=False)
            campaign.published_by = request.user
            campaign.save()
            print("Campaign updated successfully!")
            messages.success(request, "Succesfuly updated the document !")

            return redirect('campaignmanagment:campaign_detail', pk=campaign.id)
        else:
            print(f"Error updating campaign !!! {campaign_form.errors}")
            messages.error(request, "Error occured while tried to update new document !")
    else:
        campaign_form = EditCampaignForm(instance=campaign)

    return render(request, 'forms.html', context={
        'campaign_form': campaign_form,
        'title': 'Edit Campaign'
    })




@login_required
def campaign_detail_view(request, pk):
    campaign = get_object_or_404(NewCampaignModel, pk=pk)
    messages.info(request, "This is the DetailView Page of the Document")

    return render(request, 'detailview.html', {'campaign': campaign})



@login_required
def delete_view(request, pk):
    campaign = get_object_or_404(NewCampaignModel, pk=pk, published_by=request.user)
    campaign.delete()
    messages.error(request, "Document just got deleted !")

    return redirect('campaignmanagment:campaigns_form')



