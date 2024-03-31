from django.db import models
from django.contrib.auth.models import User

class OfferModel(models.Model):
    OFFER_TYPE_CHOICES = [
        ('H', 'Hotel'),
        ('V', 'Vacations'),
        ('P', 'Places'),
    ]

    STATUS_CHOICES = [
        ('C', 'Created'),
        ('R', 'Running / Active'),
        ('F', 'Finished'),
    ]

    offer_name = models.CharField(max_length=100)
    destination_place = models.CharField(max_length=100, blank=True)
    offer_description = models.TextField()
    offer_type = models.CharField(choices=OFFER_TYPE_CHOICES, max_length=1)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    duration = models.DecimalField(max_digits=100, decimal_places=2)
    price = models.IntegerField()
    status = models.CharField(choices=STATUS_CHOICES, max_length=1)
    published_by = models.ForeignKey(User, related_name='offers_authot', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.offer_name
