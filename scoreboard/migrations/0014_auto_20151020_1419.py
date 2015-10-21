# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0013_remove_score_column'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='id',
        ),
        migrations.AddField(
            model_name='score',
            name='column',
            field=models.OneToOneField(primary_key=True, default=1, serialize=False, to='scoreboard.Column'),
            preserve_default=False,
        ),
    ]
