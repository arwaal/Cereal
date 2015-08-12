# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maim', '0003_auto_20150802_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrifact',
            name='calories',
            field=models.IntegerField(null=True),
        ),
    ]
