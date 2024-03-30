from .models import NewCampaignModel
from django import forms



TEXT_CLASSES = "text-white"
INPUT_CLASSES = "py-2 px-8 rounded-2xl border bg-gray-700"
SELECT_CLASSES = "py-2 px-12 rounded-2xl border bg-gray-700"



class NewCampaignForm(forms.ModelForm):
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('P', 'Pending'),
    )
    status = forms.ChoiceField(
        label='Status',
        choices=STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': SELECT_CLASSES}),
    )


    # PLATFORM_CHOICES = (
    #     (None, "-- None --"),
    #     ("FB", "Facebook"),
    #     ("IG", "Instagram"),
    #     ("GO", "Google"),
    #     ("BI", "Bing"),
    #     ("Tk", "TikTok"),
    # )

    # platfrom = forms.ChoiceField(
    #     label='Platform',
    #     choices=PLATFORM_CHOICES,
    #     required=True,
    #     widget=forms.Select(attrs={'class': SELECT_CLASSES}),
    # )
       


    class Meta:
        model = NewCampaignModel
        fields = ('campaignname', 'titlename', 'objectives', 'budget', 'status')
        widgets = {
            'campaignname': forms.TextInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Enter Campaign Type',
            }),
            'titlename': forms.TextInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Enter Title',
            }),
            'objectives': forms.Textarea(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Enter Campaign Objectives',
            }),
            'budget': forms.NumberInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Enter Campaign Budget',
            'type': 'number'
            }),
        }



class EditCampaignForm(forms.ModelForm):
    STATUS_CHOICES = (
        ('A', 'Active'),
        ('P', 'Pending'),
    )
    status = forms.ChoiceField(
        label='Status',
        choices=STATUS_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': SELECT_CLASSES}),
    )


    # PLATFORM_CHOICES = (
    #     (None, "-- None --"),
    #     ("FB", "Facebook"),
    #     ("IG", "Instagram"),
    #     ("GO", "Google"),
    #     ("BI", "Bing"),
    #     ("Tk", "TikTok"),
    # )

    # platfrom = forms.ChoiceField(
    #     label='Platform',
    #     choices=PLATFORM_CHOICES,
    #     required=True,
    #     widget=forms.Select(attrs={'class': SELECT_CLASSES}),
    # )
       


    class Meta:
        model = NewCampaignModel
        fields = ('campaignname', 'titlename', 'objectives', 'budget', 'status')
        widgets = {
            'campaignname': forms.TextInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Enter Campaign Name',
            }),
            'titlename': forms.TextInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Enter Title',
            }),
            'objectives': forms.Textarea(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Enter Campaign Objectives',
            }),
            'budget': forms.NumberInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Enter Campaign Budget',
            }),
        }