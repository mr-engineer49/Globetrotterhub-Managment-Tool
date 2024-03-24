from django.db import models

# Create your models here.

class ImageModel(models.Model):
    images = models.ImageField(blank=True, upload_to='images/')

    
    def __str__(self):
        return str(self.id)
