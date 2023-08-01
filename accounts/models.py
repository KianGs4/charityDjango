from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    address = models.TextField(blank=True, null=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
