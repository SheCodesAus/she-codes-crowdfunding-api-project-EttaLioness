# Generated by Django 4.1.5 on 2023-01-28 01:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0006_alter_project_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 27, 12, 10, 51, 565099)),
        ),
    ]
