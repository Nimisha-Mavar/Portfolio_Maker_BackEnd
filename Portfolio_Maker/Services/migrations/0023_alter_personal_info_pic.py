# Generated by Django 4.1.5 on 2023-03-28 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0022_remove_personal_info_portfolio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='Pic',
            field=models.ImageField(blank=True, null=True, upload_to='Personal_Pic'),
        ),
    ]
