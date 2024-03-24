from .models import  NewCampaignModel
from django import forms



class NewCampaignForm(forms.ModelForm):
    class Meta:
        model = NewCampaignModel
        fields = ('campaignname', 'objectives', 'budget', 'gender', 'age_group', 'location', 'platform')
        widgets = {
            'campaignname': forms.TextInput(attrs={
                "placeholder": "Enter Campaign Name"
            }),
            'objectives': forms.TextInput(attrs={
                "placeholder": "Enter Campaign Name"
            }),
            'budget': forms.TextInput(attrs={
                "placeholder": "Enter Campaign Name"
            }),
            'gender': forms.TextInput(attrs={
                "placeholder": "Enter Campaign Name"
            }),
            'age_group': forms.TextInput(attrs={
                "placeholder": "Enter Campaign Name"
            }),
            'location': forms.TextInput(attrs={
                "placeholder": "Enter Campaign Name"
            }),
            'platform': forms.TextInput(attrs={
            "placeholder": "Enter Campaign Name"
            })
        }




