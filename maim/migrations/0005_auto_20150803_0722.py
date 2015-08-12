# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maim', '0004_auto_20150802_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cereal',
            name='t_ype',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
