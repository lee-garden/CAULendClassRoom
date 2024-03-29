# Generated by Django 2.2.6 on 2019-10-31 05:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='Building_name',
            new_name='building_name',
        ),
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_no', models.CharField(max_length=4)),
                ('floor', models.IntegerField(default=1)),
                ('capacity', models.IntegerField(default=0)),
                ('building_no', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Building')),
            ],
            options={
                'unique_together': {('building_no', 'room_no')},
            },
        ),
    ]
