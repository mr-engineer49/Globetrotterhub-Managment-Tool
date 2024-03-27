from .models import NewCampaignModel
from django import forms



TEXT_CLASSES = "text-white"
INPUT_CLASSES = "py-2 px-8 rounded-2xl border bg-gray-700"
SELECT_CLASSES = "py-2 px-12 rounded-2xl border bg-gray-700"



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


    PLATFORM_CHOICES = (
        (None, "-- None --"),
        ("FB", "Facebook"),
        ("IG", "Instagram"),
        ("GO", "Google"),
        ("BI", "Bing"),
        ("Tk", "TikTok"),
    )

    platfrom = forms.ChoiceField(
        label='Platform',
        choices=PLATFORM_CHOICES,
        required=True,
        widget=forms.Select(attrs={'class': SELECT_CLASSES}),
    )
       


    class Meta:
        model = NewCampaignModel
        fields = ('campaignname', 'objectives', 'budget', 'status', 'platfrom')
        widgets = {
            'campaignname': forms.TextInput(attrs={
            'class': INPUT_CLASSES,
            'placeholder': 'Enter Campaign Name',
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