from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class NewClientModel(models.Model):
    BOOKING_TYPE_CHOICES = [
        ('H', 'Hotel'),
        ('V', 'Vacations'),
        ('P', 'Places'),
    ]

    PHASE_CHOICES = [
        ('C', 'Created'),
        ('R', 'Running / Active'),
        ('F', 'Finished'),
    ]

    default_user_id = User.objects.first().id

    fullname = models.CharField(blank=True, max_length=50)
    email = models.EmailField(blank=True)
    phone_no = models.IntegerField(blank=True, max_length=15)
    start_date_client = models.DateTimeField(auto_now_add=True, null=True)
    end_date_client = models.DateTimeField(auto_now_add=True, null=True)
    booking_type = models.CharField(blank=True, default=BOOKING_TYPE_CHOICES, max_length=50)
    place = models.CharField(blank=True, max_length=50)
    price = models.IntegerField(blank=True)
    phase = models.CharField(blank=True, default=PHASE_CHOICES, max_length=50)
    published_by = models.ForeignKey(User, related_name='client_author', on_delete=models.CASCADE, default=default_user_id)
    is_active = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname
