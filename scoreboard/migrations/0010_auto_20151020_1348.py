# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0009_auto_20151020_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='column',
            name='score',
        ),
        migrations.AddField(
            model_name='score',
            name='column',
            field=models.ManyToManyField(related_name='score', null=True, to='scoreboard.Column', blank=True),
            preserve_default=True,
        ),
    ]
