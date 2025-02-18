# Generated by Django 5.1.3 on 2025-02-05 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0007_booking_model_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_model',
            name='booking_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Confirmed', 'Confirmed'), ('Cancelled', 'Cancelled')], default='Pending', max_length=50),
        ),
    ]
