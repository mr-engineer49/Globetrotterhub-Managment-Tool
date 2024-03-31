from .models import NewClientModel
from django import forms

TEXT_CLASSES = "text-white"
INPUT_CLASSES = "py-2 px-8 rounded-2xl border bg-gray-700 text-white"
SELECT_CLASSES = "py-2 px-12 rounded-2xl border bg-gray-700 text-white"

class ClientFormBase(forms.ModelForm):
    TYPE_CHOICES = (
        ('H', 'Hotel'),
        ('V', 'Vacations'),
        ('P', 'Places'),
    )
    booking_type = forms.ChoiceField(
        label='Booking Type',
        choices=TYPE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': SELECT_CLASSES}),
    )

    PHASE_CHOICES = (
        ('C', 'Created'),
        ('R', 'Running / Active'),
        ('F', 'Finished'),
    )
    phase = forms.ChoiceField(
        label='Phase',
        choices=PHASE_CHOICES,
        required=False,
        widget=forms.Select(attrs={'class': SELECT_CLASSES}),
    )

    class Meta:
        model = NewClientModel
        fields = ('fullname', 'email', 'phone_no', 'booking_type', 'phase', 'place', 'price', 'is_active', 'is_pending')
        widgets = {
            'fullname': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'email': forms.EmailInput(attrs={'class': INPUT_CLASSES}),
            'phone_no': forms.TextInput(attrs={'class': INPUT_CLASSES, 'id':'phone', 'name':'phone'}),
            'place': forms.TextInput(attrs={'class': INPUT_CLASSES}),
            'price': forms.NumberInput(attrs={'class': INPUT_CLASSES}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
            'is_pending': forms.CheckboxInput(attrs={'class': 'form-checkbox'}),
        }

class NewClientForm(ClientFormBase):
    pass
