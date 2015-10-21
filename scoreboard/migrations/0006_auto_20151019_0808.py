# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0005_auto_20151019_0805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='denominator',
        ),
        migrations.RemoveField(
            model_name='score',
            name='numerator',
        ),
    ]
