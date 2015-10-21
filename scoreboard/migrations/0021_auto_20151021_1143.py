# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0020_column_weight'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='points',
            new_name='score',
        ),
    ]
