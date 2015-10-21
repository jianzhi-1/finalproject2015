# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoreboard', '0003_remove_student_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='points',
            field=models.ManyToManyField(related_name='student', null=True, to='scoreboard.Score', blank=True),
            preserve_default=True,
        ),
    ]
