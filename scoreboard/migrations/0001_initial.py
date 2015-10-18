# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('header', models.CharField(max_length=255)),
                ('color', models.CharField(default=b'yellow', max_length=50)),
                ('fontcolor', models.CharField(default=b'black', max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('numerator', models.CharField(max_length=10)),
                ('denominator', models.CharField(max_length=10)),
                ('column', models.ForeignKey(blank=True, to='scoreboard.Column', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Scoreboard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('sid', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('color', models.CharField(default=b'yellow', max_length=50)),
                ('fontcolor', models.CharField(default=b'black', max_length=50)),
                ('columns', models.ManyToManyField(related_name='scoreboard', null=True, to='scoreboard.Column')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('points', models.ForeignKey(blank=True, to='scoreboard.Score', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='scoreboard',
            name='student',
            field=models.ManyToManyField(related_name='scoreboard', null=True, to='scoreboard.Student', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='scoreboard',
            name='user',
            field=models.ForeignKey(blank=True, to='accounts.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
