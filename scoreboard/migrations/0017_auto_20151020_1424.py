# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0016_score_column'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='column',
        ),
        migrations.RemoveField(
            model_name='score',
            name='denominator',
        ),
        migrations.RemoveField(
            model_name='score',
            name='numerator',
        ),
        migrations.AddField(
            model_name='score',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]
