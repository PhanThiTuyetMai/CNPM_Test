# Generated by Django 4.2.11 on 2024-03-25 18:20

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_alter_course_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=cloudinary.models.CloudinaryField(max_length=255),
        ),
    ]