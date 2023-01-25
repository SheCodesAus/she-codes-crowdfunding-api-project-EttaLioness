from django.db import models
from django.contrib.auth import get_user_model #Django will find what model you are using
#from datetime import timedelta #,datetime, 


User = get_user_model()
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
    ("Political Sc", "Political Science")
    
)
class Project(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    goal=models.FloatField()
    question_one = models.TextField() #added
    question_two = models.TextField() #added
    question_three = models.TextField() #added
    image=models.URLField()
    video=models.URLField()
    is_open=models.BooleanField()
    # date_created=models.DateTimeField(auto_now_add=True)    #(auto_now_add=True) datetime.now()
    # end_date = date_created + \
    #     timedelta(days = 30)
    #(above)tells django when created to add at current time
    category = models.CharField(max_length=200, null=True, choices= CATEGORIES)
    project_email = models.EmailField()
    #choices-A sequence of 2-tuples to use as choices for this field. 
    # The default form widget will be a select box instead of the standard limited to the choices given.
    # The first element in tuple is value stored database. The second displayed by the field’s form widget.
    innovation_star = models.ManyToManyField( #added
        User,
        related_name="innovation_star_projects"
    )

    @property #added
    def total_stars(self):
        return self.pledges.aggregate(sum=models.Sum('amount'))['sum']

    @property #added for pleged so far
    def total_amount_pledged(self):
        return self.pledges.aggregate(sum=models.Sum('amount'))['sum']

    owner=models.ForeignKey( #need to change this (above) to foreignKey(other table primary key),user id
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
        related_name="supporter_pledges"
    )
