# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0017_auto_20151020_1424'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='name',
        ),
        migrations.AddField(
            model_name='score',
            name='denominator',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='score',
            name='numerator',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
