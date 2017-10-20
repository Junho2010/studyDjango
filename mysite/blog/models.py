from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft','Draft'),
        ('published','Published')
    )

    title  = models.CharField(max_length=250)
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 

