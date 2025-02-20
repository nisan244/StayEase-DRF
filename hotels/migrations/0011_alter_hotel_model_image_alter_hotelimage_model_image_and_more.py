# Generated by Django 5.1.3 on 2025-02-20 10:08

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0010_alter_hotelimage_model_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel_model',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='hotels/image'),
        ),
        migrations.AlterField(
            model_name='hotelimage_model',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='hotels/extra_images'),
        ),
        migrations.AlterField(
            model_name='room_model',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='rooms/image'),
        ),
        migrations.AlterField(
            model_name='roomimage_model',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='rooms/extra_images'),
        ),
    ]
