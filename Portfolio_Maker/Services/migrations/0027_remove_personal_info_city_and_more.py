# Generated by Django 4.1.5 on 2023-04-23 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0026_personal_info_city_personal_info_state_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personal_info',
            name='City',
        ),
        migrations.RemoveField(
            model_name='personal_info',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='personal_info',
            name='State',
        ),
    ]
