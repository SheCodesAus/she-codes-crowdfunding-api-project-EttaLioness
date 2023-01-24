from django.db import models

from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    image = models.URLField(default = "https://i.postimg.cc/rm82XhCm/default-profile-image.png") #added
    #https://pypi.org/project/django-default-imagefield/
    # if deploying to a production environment, you must run the ./manage.py collectstatic command to copy
    #  the image files included in the package to the static file serving path
    bio = models.TextField(blank=True) #added
    qualifications = models.TextField(blank=True) #added
    affiliate = models.CharField(max_length=200, blank=True) #added

    def __str__(self):
        return self.username