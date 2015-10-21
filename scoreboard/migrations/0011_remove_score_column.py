# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0010_auto_20151020_1348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='column',
        ),
    ]
