# Generated by Django 4.1.5 on 2023-04-02 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_remove_payment_order_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='Total',
            field=models.FloatField(default=0),
        ),
    ]
