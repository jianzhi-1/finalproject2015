# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0026_scoreboard_sid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreboard',
            name='sid',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
