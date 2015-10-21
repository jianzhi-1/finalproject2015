# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0004_student_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='score',
            name='denominator',
            field=models.IntegerField(),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='score',
            name='numerator',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
