# Generated by Django 2.2.6 on 2019-12-03 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20191118_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='building',
            name='max_floor',
            field=models.IntegerField(default=12),
        ),
        migrations.AlterField(
            model_name='building',
            name='min_floor',
            field=models.IntegerField(default=-8),
        ),
    ]
