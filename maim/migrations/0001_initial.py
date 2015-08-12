# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cereal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('serving_size_weight', models.FloatField()),
                ('cups_per_serving', models.FloatField()),
                ('display_shelf', models.FloatField()),
                ('t_ype', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NutriFact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calories', models.FloatField()),
                ('protein', models.FloatField()),
                ('fat', models.FloatField()),
                ('sodium', models.FloatField()),
                ('dietary_fiber', models.FloatField()),
                ('carbs', models.FloatField()),
                ('sugars', models.FloatField()),
                ('potassium', models.FloatField()),
                ('vitamins', models.FloatField()),
                ('Cereal', models.OneToOneField(to='maim.Cereal')),
            ],
        ),
        migrations.AddField(
            model_name='cereal',
            name='manufacturer',
            field=models.ForeignKey(to='maim.Manufacturer'),
        ),
    ]
