# Generated by Django 4.1.5 on 2023-01-28 05:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_alter_project_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 27, 16, 46, 40, 95325)),
        ),
    ]
