from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    meetup_address = models.CharField(max_length= 250)
