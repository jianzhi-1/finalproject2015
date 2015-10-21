# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0002_auto_20151018_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='points',
        ),
    ]
