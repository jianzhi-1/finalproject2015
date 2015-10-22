# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0025_auto_20151022_0552'),
    ]

    operations = [
        migrations.AddField(
            model_name='scoreboard',
            name='sid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
