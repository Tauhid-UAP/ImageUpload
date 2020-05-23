from django.db import models
from django.utils import timezone

# Create your models here.

class Photo(models.Model):
    pub_date = timezone.now()
    image = models.ImageField(upload_to='images')
