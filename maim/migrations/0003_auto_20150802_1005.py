# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maim', '0002_auto_20150802_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='cups_per_serving',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='display_shelf',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='manufacturer',
            field=models.ForeignKey(to='maim.Manufacturer', null=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='name',
            field=models.CharField(max_length=50, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='serving_size_weight',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='cereal',
            name='t_ype',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='manufacturer',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='nutrifact',
            name='Cereal',
            field=models.OneToOneField(null=True, to='maim.Cereal'),
        ),
        migrations.AlterField(
            model_name='nutrifact',
            name='calories',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrifact',
            name='carbs',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrifact',
            name='dietary_fiber',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrifact',
            name='fat',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrifact',
            name='potassium',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrifact',
            name='protein',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrifact',
            name='sodium',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrifact',
            name='sugars',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='nutrifact',
            name='vitamins',
            field=models.FloatField(null=True),
        ),
    ]
