from django.db import models
from django.contrib.auth import get_user_model #Django will find what model you are using
from datetime import datetime, timedelta


User = get_user_model()

    #choices-A sequence of 2-tuples to use as choices for this field. 
    # The default form widget will be a select box instead of the standard limited to the choices given.
    # The first element in tuple is value stored database. The second displayed by the field’s form widget.

CATEGORIES = (
    ("Eng", "Engineering"),
    ("Chem", "Chemistry"),
    ("Bio", "Biology"),
    ("Math", "Mathematics"),
    ("Social Sci", "Social Sciences"),
    ("Ecom", "Economic"),
    ("Data Sc", "Data Science"),
    ("Comp Sci", "Computer Science"),
    ("Ecology", "Ecology"),
    ("Physics", "Physics"),
    ("Materials Sc", "Material Science"),
    ("Earth Sci", "Earth Science"), 
    ("Edu", "Education"),
    ("Paleo", "Paleontology"),
    ("Med", "Medicine"),
    ("Neuro", "Neuroscience"),
    ("Psych", "Pschycology"),
    ("Anthropology", "Anthropology"),
    ("Art and Design", "Art and Design"),
    ("Political Sc", "Political Science"),
    ("Astro", "Astrophysics")
    
)
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    goal=models.FloatField()
    question_one = models.TextField() #added
    question_two = models.TextField() #added
    question_three = models.TextField() #added
    image=models.URLField(default="https://i.postimg.cc/pLgqMZxh/test-g95215e4ee-1280.jpg")
    video=models.URLField()
    is_open=models.BooleanField(default=True)
    #date_created=models.DateTimeField(datetime.now())    #(auto_now_add=True) datetime.now()
    date_created = models.DateTimeField(default=datetime.now)
    end_date = models.DateTimeField(default=(datetime.now() + timedelta(days=30)))
    #(above)tells django when created to add at current time
    category = models.CharField(max_length=200, null=True, choices= CATEGORIES)
    project_email = models.EmailField()
    innovation_star = models.ManyToManyField( #added
        User,
        related_name="innovation_star_projects"
    )
    #    # NEED TO ADD amount_pledged = models.ManyToManyField( User, related_name = "pledges") 
    # #add to serializer too amount_pledged#

    @property #added , look up decorators
    def total_stars(self):
        return self.innovation_star_projects.aggregate(sum=models.Sum('amount'))['sum']

    @property #added for pledged so far
    def total_amount_pledged(self):
        return self.pledges.aggregate(sum=models.Sum('amount'))['sum']

    owner=models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="owner_projects"
    )

class Pledge(models.Model):
    amount =models.FloatField()
    comment = models.CharField(max_length=200)
    anonymous = models.BooleanField()
    project = models.ForeignKey(
        'Project',
        on_delete=models.CASCADE,
        related_name="pledges" #get the pledges list added as attribute
    )
    supporter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="supporters_of_project"
    )
