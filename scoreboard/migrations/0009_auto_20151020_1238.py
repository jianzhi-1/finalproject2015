# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0008_auto_20151020_0344'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='column',
        ),
        migrations.AddField(
            model_name='column',
            name='score',
            field=models.ManyToManyField(related_name='column', null=True, to='scoreboard.Score', blank=True),
            preserve_default=True,
        ),
    ]
