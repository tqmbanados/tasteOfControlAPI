# Generated by Django 4.0.3 on 2022-05-04 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_instrument_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='stage',
            field=models.CharField(default='0-0', max_length=16),
        ),
    ]
