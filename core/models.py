from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.

AGE_CHOICES = (
    ('All', 'All'),
    ('Kids', 'Kids'),
)

MOVIE_CHOICES = (
    ('single','Single'),
    ('seasonal','Seasonal')
)

class CustomUser(AbstractUser):
    profiles = models.ManyToManyField('Profile', blank=True)

class Profile(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    age_limit = models.CharField(max_length=10, choices=AGE_CHOICES)
    uuid = models.UUIDField(default=uuid.uuid4)

class Movie(models.Model):
    name =models.CharField(max_length=255, null=False, blank=False)
    description = models.TextField(max_length=1500, null=False, blank=False)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    type = models.CharField(max_length=10, choices=MOVIE_CHOICES)
    videos = models.ManyToManyField('Video')
    flyer = models.ImageField(upload_to='flyers',blank=True,null=True)
    age_limit = models.CharField(max_length=5,choices=AGE_CHOICES,blank=True,null=True)

class Video(models.Model):
    title = models.CharField(max_length=225,blank=True,null=True)
    files = models.FileField(upload_to='movies')