from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    # bio = model.TextField()

    def __str__(self):
        return self.username