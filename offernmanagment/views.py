from django.shortcuts import render
from django.shortcuts import  render, redirect, get_object_or_404
from .forms import NewOfferForm
from .models import OfferModel
from django.contrib.auth.decorators import  login_required

# Create your views here.

def offers_view(request):
    offers = OfferModel.objects.filter(published_by=request.user)
    return render (request, 'offers.html', context={
        'offers':offers
    })


@login_required
def offers_detail_view(request, pk):
    offer = get_object_or_404(OfferModel, pk=pk)
    return render(request, 'offers_detail.html', context={
        'offer':offer
    })



@login_required
def new_offer_view(request):
    if request.method == "POST":
        offer_form = NewOfferForm(request.POST, request.FILES)
        
        if offer_form.is_valid():
            offer = offer_form.save(commit=False)
            offer.published_by = request.user
            offer.save()
            print("new offer created!")

            return redirect("offernmanagment:offers_form", pk=offer.id)
        else:
            print(f"Error creating new offer !!! {offer_form.errors}")
    else:
        offer_form = NewOfferForm()

    return render (request, "offers_form.html", context={
        "offer_form":offer_form,
        'title': 'Add New Offer'
        })

