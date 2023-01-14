from django.db import models

# Create your models here.
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    goal=models.FloatField()
    image=models.URLField()
    video=models.URLField()
    is_open=models.BooleanField()
    date_created=models.DateTimeField(auto_now_add=True) 
    #(above)tells django when created to add at current time
    owner=models.CharField(max_length=200)
    #need to change this (above) to foreignKey(other table primary key),user id


class Pledge(models.Model):
    amount =models.FloatField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name="pledges" #get the pledges list added as attribute
    )
    supporter = models.CharField(max_length=200)
