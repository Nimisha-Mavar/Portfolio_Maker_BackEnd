# Generated by Django 4.1.5 on 2023-03-24 01:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0016_alter_experience_portfolio_alter_experience_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='End_year',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='End_year',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='End_year',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
