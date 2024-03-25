# Generated by Django 4.2.11 on 2024-03-25 18:40

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_tag_lesson_comment_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar',
            field=cloudinary.models.CloudinaryField(default='https://res.cloudinary.com/duz2xltvs/image/upload/v1711390925/unghi7vkrcec7tx1fhbr.jpg', max_length=255),
        ),
    ]