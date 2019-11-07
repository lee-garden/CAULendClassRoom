# Generated by Django 2.2.6 on 2019-11-07 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20191107_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='building_no',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='room_no',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.ClassRoom'),
        ),
    ]
