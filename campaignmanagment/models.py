from django.db import models

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
    
    PLATFORM_CHOICES = [
        ('F', 'Facebook'),
        ('I', 'Instagram'),
        ('X', 'X (Twitter)'),
        ('T', 'TikTok'),
    ]

    campaignname = models.CharField(blank=True, max_length=50)
    objectives = models.TextField(blank=True, max_length=10000)
    budget = models.FloatField(blank=True, max_length=100000000)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age_group = models.CharField(max_length=1, choices=AGE_GROUP_CHOICES)
    location = models.CharField(max_length=1, choices=LOCATION_CHOICES)
    platform = models.CharField(max_length=1, choices=PLATFORM_CHOICES)

    def __str__(self):
        return self.campaignname
