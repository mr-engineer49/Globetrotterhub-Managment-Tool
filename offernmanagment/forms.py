from .models import OfferModel
from django import forms

TEXT_CLASSES = "text-white"
INPUT_CLASSES = "py-2 px-8 rounded-2xl border bg-gray-700 text-white w-32"
SELECT_CLASSES = "py-2 px-12 rounded-2xl border bg-gray-700 text-white"

class OfferFormBase(forms.ModelForm):
    TYPE_CHOICES = (
        ('Hotel', 'Hotel'),
        ('Vacations', 'Vacations'),
        ('Places', 'Places'),
    )
    offer_type = forms.ChoiceField(
        label='Offer Type',
        choices=TYPE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': SELECT_CLASSES}),
    )

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )
    status = forms.ChoiceField(
        label='Status',
        choices=STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': SELECT_CLASSES}),
    )

    class Meta:
        model = OfferModel
        fields = ('offer_name', 'offer_description', 'destination_place', 'offer_type', 'price', 'duration', 'discount', 'status')
        widgets = {
            'offer_name': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'offer_description': forms.Textarea(attrs={'class': INPUT_CLASSES}),
            'discount': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'destination_place': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'price': forms.NumberInput(),
            'duration': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
        }

class NewOfferForm(OfferFormBase):
    pass
