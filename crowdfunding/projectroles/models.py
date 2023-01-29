from django.db import models
from django.contrib.auth import get_user_model #Django will find what model you are using


User = get_user_model()

class Projectroles(models.Model):
    description = models.CharField(max_length=200)
    member = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="member_role"
    )
    project = models.ForeignKey(
        'projects.Project',
        on_delete=models.CASCADE,
        related_name="roles" #get the pledges list added as attribute
    )
    creator = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="creator_of_role"
    )