from django.shortcuts import  render, redirect, get_object_or_404
from .forms import NewCampaignForm, EditCampaignForm
from .models import NewCampaignModel
from django.contrib.auth.decorators import  login_required




# Create your views here.
@login_required()
def campaigns_view(request):
    campaigns = NewCampaignModel.objects.filter()
    return render(request, 'campaigns.html', context={
        'campaigns':campaigns,
    })



@login_required()
def new_campaign_view(request):
    if request.method == "POST":
        new_campaign_form = NewCampaignForm(request.POST, request.FILES)
        
        if new_campaign_form.is_valid():
            campaign = new_campaign_form.save(commit=False)
            campaign.published_by = request.user
            campaign.save()
            print("new campaign created!")

            return redirect("campaignmanagment:campaign_detail", pk=campaign.id)
        else:
            print(f"Error creating new campaign !!! {new_campaign_form.errors}")
    else:
        new_campaign_form = NewCampaignForm()

    return render (request, "campaigns.html", context={
        "new_campaign_form":new_campaign_form,
        })




@login_required
def edit_campaign_view(request, pk):
    campaign = get_object_or_404(NewCampaignModel, pk=pk, published_by=request.user)

    if request.method == 'POST':
        edit_campaign_form = EditCampaignForm(request.POST, request.FILES, instance=campaign)

        if edit_campaign_form.is_valid():
            campaign = edit_campaign_form.save(commit=False)
            campaign.published_by = request.user
            campaign.save()
            print("Campaign updated successfully!")

            return redirect('campaignmanagment:campaign_detail', pk=campaign.id)
        else:
            print(f"Error updating campaign !!! {edit_campaign_form.errors}")
    else:
        edit_campaign_form = EditCampaignForm(instance=campaign)

    return render(request, 'forms.html', context={
        'edit_campaign_form': edit_campaign_form,
    })




@login_required
def campaign_detail_view(request, pk):
    campaign = get_object_or_404(NewCampaignModel, pk=pk)
    return render(request, 'detailview.html', {'campaign': campaign})



@login_required
def delete_view(request, pk):
    campaign = get_object_or_404(NewCampaignModel, pk=pk, published_by=request.user)
    campaign.delete()

    return redirect('campaignmanagment:campaigns_form')



