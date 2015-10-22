# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0023_auto_20151021_1149'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='scoreboard',
            name='sid',
        ),
    ]
