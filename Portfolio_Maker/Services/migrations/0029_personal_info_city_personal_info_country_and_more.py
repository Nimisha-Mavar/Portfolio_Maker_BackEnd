# Generated by Django 4.1.5 on 2023-04-23 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0028_education_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_info',
            name='City',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='Country',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='personal_info',
            name='State',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
