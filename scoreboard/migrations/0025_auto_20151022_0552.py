# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0024_remove_scoreboard_sid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='denominator',
        ),
        migrations.AddField(
            model_name='column',
            name='denominator',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
