# Generated by Django 4.1.5 on 2023-01-28 01:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_project_innovation_star_project_project_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
