# Generated by Django 4.0.5 on 2022-11-29 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0013_alter_booking_amount_paid'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
