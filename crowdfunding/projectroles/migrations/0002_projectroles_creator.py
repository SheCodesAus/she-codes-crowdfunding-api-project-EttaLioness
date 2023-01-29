# Generated by Django 4.1.5 on 2023-01-29 01:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projectroles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectroles',
            name='creator',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='creator_of_role', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
