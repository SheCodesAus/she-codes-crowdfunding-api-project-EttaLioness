# Generated by Django 4.1.5 on 2023-01-24 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_customuser_image_alter_customuser_affiliate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='affiliate',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='qualifications',
            field=models.TextField(null=True),
        ),
    ]
