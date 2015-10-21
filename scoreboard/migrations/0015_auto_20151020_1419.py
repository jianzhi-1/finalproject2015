# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0014_auto_20151020_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='score',
            name='column',
        ),
        migrations.AddField(
            model_name='score',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, default=1, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]
