# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0021_auto_20151021_1143'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='score',
            new_name='points',
        ),
    ]
