from django.db import models
from django.contrib.auth.models import User




class NewCampaignModel(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    AGE_GROUP_CHOICES = [
        ('T', 'Teen'),
        ('A', 'Adult'),
        ('O', 'Old'),
    ]
    
    LOCATION_CHOICES = [
        ('E', 'Europe'),
        ('U', 'USA'),
        ('A', 'Asia'),
    ]
    

    campaignname = models.CharField(blank=True, max_length=50)
    titlename = models.CharField(blank=True, max_length=50)
    objectives = models.TextField(blank=True, max_length=10000)
    budget = models.FloatField(blank=True, max_length=100000000)
    gender = models.BooleanField(default=False, blank=True)  # True for Male, False for Female
    age = models.BooleanField(default=False, blank=True)     # True for Teen, False for Adult/Old
    location = models.BooleanField(default=False, blank=True)   # True for Europe, False for USA/Asia
    start_date = models.DateTimeField(auto_now_add=True, null=True)
    end_date = models.DateTimeField(auto_now_add=True, null=True)
    published_by = models.ForeignKey(User, related_name='campaigns_author', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_pending = models.BooleanField(default=True)

    def __str__(self):
        return self.campaignname
