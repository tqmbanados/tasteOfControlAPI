# Generated by Django 4.0.3 on 2022-05-17 03:59

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_actor_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='image_data',
            field=models.ImageField(max_length='64', null=True, upload_to=backend.models.upload_to),
        ),
    ]
