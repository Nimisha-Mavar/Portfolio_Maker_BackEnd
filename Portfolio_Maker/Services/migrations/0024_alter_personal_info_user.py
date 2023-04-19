# Generated by Django 4.1.5 on 2023-03-30 14:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Services', '0023_alter_personal_info_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='personal_info',
            name='User',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]