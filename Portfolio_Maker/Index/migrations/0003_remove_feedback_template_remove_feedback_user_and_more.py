# Generated by Django 4.1.5 on 2023-03-05 17:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("Index", "0002_feedback"),
    ]

    operations = [
        migrations.RemoveField(model_name="feedback", name="Template",),
        migrations.RemoveField(model_name="feedback", name="User",),
        migrations.AlterField(
            model_name="feedback", name="Rate", field=models.IntegerField(default=0),
        ),
    ]