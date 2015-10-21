# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0018_auto_20151020_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='column',
            field=models.ForeignKey(blank=True, to='scoreboard.Column', null=True),
            preserve_default=True,
        ),
    ]
