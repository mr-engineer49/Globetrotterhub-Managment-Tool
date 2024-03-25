from .models import NewCampaignModel
from django import forms

INPUT_CLASSES = "py-4 px-8 rounded-2xl border"

class NewCampaignForm(forms.ModelForm):
    class Meta:
        model = NewCampaignModel
        fields = ('campaignname', 'objectives', 'budget')
        # widgets = {
        #     'campaignname': forms.TextInput(attrs={
        #         'class': INPUT_CLASSES,
        #         'placeholder': 'Enter Campaign Name',
        #     }),
        #     'objectives': forms.Textarea(attrs={
        #         'class': INPUT_CLASSES,
        #         'placeholder': 'Enter Campaign Objectives',
        #     }),
        #     'budget': forms.NumberInput(attrs={
        #         'class': INPUT_CLASSES,
        #         'placeholder': 'Enter Campaign Budget',
        #     }),
        #     # 'gender': forms.Select(attrs={
        #     #     'class': INPUT_CLASSES,
        #     # }),
        #     # 'age_group': forms.Select(attrs={
        #     #     'class': INPUT_CLASSES,
        #     # }),
        #     # 'location': forms.Select(attrs={
        #     #     'class': INPUT_CLASSES,
        #     # }),
        #     # 'platform': forms.Select(attrs={
        #     #     'class': INPUT_CLASSES,
        #     # }),
        # }

        # def __init__(self, *args, **kwargs):
        #     super(NewCampaignForm, self).__init__(*args, **kwargs)
        # # Set required=False for fields that you want to be optional
        #     self.fields['gender'].required = False
        #     self.fields['age_group'].required = False
        #     self.fields['location'].required = False
        #     self.fields['platform'].required = False


