# Generated by Django 4.0.5 on 2022-11-26 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receptionist', '0003_rename_size_rooms_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('capacity', models.IntegerField()),
                ('grade', models.CharField(choices=[('Executive', 'Executive'), ('Ordinary', 'Ordinary'), ('Standard', 'Standard')], max_length=100)),
                ('price', models.IntegerField()),
                ('availability', models.BooleanField(default=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Rooms',
        ),
    ]
