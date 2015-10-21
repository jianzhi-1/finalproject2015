# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0007_auto_20151019_0819'),
    ]

    operations = [
        migrations.RenameField(
            model_name='scoreboard',
            old_name='columns',
            new_name='column',
        ),
    ]
