# Generated by Django 5.1.3 on 2025-02-02 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookings', '0004_alter_booking_model_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_model',
            name='guests',
            field=models.PositiveIntegerField(help_text='Number of guests', null=True),
        ),
    ]
