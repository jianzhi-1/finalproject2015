# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0019_score_column'),
    ]

    operations = [
        migrations.AddField(
            model_name='column',
            name='weight',
            field=models.FloatField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
