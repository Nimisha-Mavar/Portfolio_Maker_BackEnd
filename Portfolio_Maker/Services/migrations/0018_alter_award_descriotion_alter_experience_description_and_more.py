# Generated by Django 4.1.5 on 2023-03-24 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0017_alter_education_end_year_alter_experience_end_year_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='award',
            name='Descriotion',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='Description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='Description',
            field=models.TextField(null=True),
        ),
    ]
