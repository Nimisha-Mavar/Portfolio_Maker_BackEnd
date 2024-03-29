# Generated by Django 4.1.5 on 2023-03-10 09:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("Templates", "0003_alter_detail_temp_cat_alter_detail_temp_type"),
        ("Index", "0004_rename_message_feedback_message1"),
    ]

    operations = [
        migrations.RenameField(
            model_name="feedback", old_name="Date", new_name="Date1",
        ),
        migrations.RenameField(
            model_name="feedback", old_name="Rate", new_name="Rate1",
        ),
        migrations.AddField(
            model_name="feedback",
            name="Template",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to="Templates.detail",
            ),
        ),
        migrations.AddField(
            model_name="feedback",
            name="User",
            field=models.ForeignKey(
                default=0,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
