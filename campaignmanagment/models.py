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
    gender = models.BooleanField(default=False, blank=True)  # True for Male, False for Female
    age = models.BooleanField(default=False, blank=True)     # True for Teen, False for Adult/Old
    location = models.BooleanField(default=False, blank=True)   # True for Europe, False for USA/Asia
    start_date = models.DateTimeField(auto_now_add=True, null=True)
    end_date = models.DateTimeField(auto_now_add=True, null=True)


    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.campaignname
