# Generated by Django 4.1.5 on 2023-03-21 00:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Services', '0013_alter_personal_info_resume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='Portfolio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Services.portfolio'),
        ),
        migrations.AlterField(
            model_name='education',
            name='Resume',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Services.resume'),
        ),
    ]
