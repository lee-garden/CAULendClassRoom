# Generated by Django 2.2.6 on 2019-11-05 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_building_max_floor'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='min_foor',
            field=models.IntegerField(default=0),
        ),
    ]
