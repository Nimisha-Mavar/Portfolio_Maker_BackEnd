# Generated by Django 4.1.5 on 2023-02-19 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Templates', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='Temp_file',
            field=models.FileField(upload_to='Template_files'),
        ),
    ]
