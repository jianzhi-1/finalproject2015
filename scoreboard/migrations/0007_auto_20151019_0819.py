# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0006_auto_20151019_0808'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='denominator',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='score',
            name='numerator',
            field=models.IntegerField(default=2),
            preserve_default=False,
        ),
    ]
