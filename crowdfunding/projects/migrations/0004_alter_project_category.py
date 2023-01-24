# Generated by Django 4.1.5 on 2023-01-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_rename_categories_project_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='category',
            field=models.CharField(choices=[('Eng', 'Engineering'), ('Chem', 'Chemistry'), ('Bio', 'Biology'), ('Math', 'Mathematics'), ('Social Sci', 'Social Sciences'), ('Ecom', 'Economic'), ('Data Sc', 'Data Science'), ('Comp Sci', 'Computer Science'), ('Ecology', 'Ecology'), ('Physics', 'Physics'), ('Materials Sc', 'Material Science'), ('Earth Sci', 'Earth Science'), ('Edu', 'Education'), ('Paleo', 'Paleontology'), ('Med', 'Medicine'), ('Neuro', 'Neuroscience'), ('Psych', 'Pschycology'), ('Anthropology', 'Anthropology'), ('Art and Design', 'Art and Design'), ('Political Sc', 'Political Science')], max_length=200, null=True),
        ),
    ]