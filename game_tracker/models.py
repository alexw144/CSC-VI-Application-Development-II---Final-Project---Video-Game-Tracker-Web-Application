from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=15, choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], blank=True, null=True)

    def __str__(self):
        return self.user.username + "'s Profile"