# Generated by Django 4.0.5 on 2022-11-27 22:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0010_alter_booking_room_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='next_booked_date',
        ),
        migrations.RemoveField(
            model_name='room',
            name='next_free_date',
        ),
    ]
