# Generated by Django 5.1.3 on 2025-01-20 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_model',
            name='image',
            field=models.ImageField(upload_to='hotels/image/'),
        ),
    ]
