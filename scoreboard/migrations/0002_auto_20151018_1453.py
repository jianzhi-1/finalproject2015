# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scoreboard',
            name='columns',
            field=models.ManyToManyField(related_name='scoreboard', null=True, to='scoreboard.Column', blank=True),
            preserve_default=True,
        ),
    ]
