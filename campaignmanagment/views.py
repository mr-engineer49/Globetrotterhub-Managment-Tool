from django.shortcuts import  render, redirect, get_object_or_404
from django.shortcuts import  render, redirect
from .forms import NewCampaignForm, EditCampaignForm
from .models import NewCampaignModel
from django.contrib.auth.decorators import  login_required




# Create your views here.
@login_required()
def campaigns_view(request):
    new_campaign = NewCampaignModel.objects.filter(is_pending=True)
    return render(request, 'campaigns.html', context={
        'new_campaign':new_campaign,
    })



@login_required()
def new_campaign_view(request):
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



@login_required
def campaign_detail_view(request, pk):
    newcampaign = get_object_or_404(NewCampaignModel, pk=pk)
    return render(request, 'detailview.html', {'newcampaign': newcampaign})



@login_required
def edit_campaign_view(request, pk):
    edit_campaign = get_object_or_404(NewCampaignModel, pk=pk, published_by=request.user)

    if request.method == 'POST':
        edit_campaign_form = EditCampaignForm(request.POST, request.FILES, instance=edit_campaign)
        if edit_campaign_form.is_valid():
            edit_campaign = edit_campaign_form.save(commit=False)
            edit_campaign.published_by = request.user
            edit_campaign.save()

            return redirect('campaignmanagment:campaign_detail', pk=edit_campaign.id)
        
        else:

            edit_campaign_form = EditCampaignForm(instance=edit_campaign)
        return render(request, 'forms.html', {
            'edit_campaign_form': edit_campaign_form,
        })
