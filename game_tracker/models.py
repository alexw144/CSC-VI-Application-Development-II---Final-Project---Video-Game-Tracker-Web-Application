from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=15, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True, default='O')

    def __str__(self):
        return self.user.username + "'s Profile"


class Game(models.Model):
    title = models.CharField(max_length=75, blank=True)
    genre = models.CharField(max_length=50, blank=True)
    synopsis = models.TextField(default="Nothing yet, Sorry.", blank=True)
    esrb_rating = models.CharField(max_length=10, choices=[('E', 'Everyone'), ('E10', 'Everyone 10+'), ('T', 'Teen'), ('M', 'Mature 17+'), ('A', 'Adult Only 18+'), ('RP', 'Rating Pending'), ('RPM', 'Rating Pending Likely Mature 17+'), ('O', 'Other')], blank=True, default='O')
    developer = models.CharField(max_length=25, blank=True)
    publisher = models.CharField(max_length=25, blank=True)
    playstation = models.BooleanField(null=True)
    xbox = models.BooleanField(null=True)
    switch = models.BooleanField(null=True)
    pc = models.BooleanField(null=True)
    other = models.BooleanField(null=True)
    release_date = models.DateField(null=True, blank=True)
    game_cover_image = models.ImageField(default='fallback.png', blank=True)

    def __str__(self):
        return self.title