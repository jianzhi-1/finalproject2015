# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0012_score_column'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='column',
        ),
    ]
