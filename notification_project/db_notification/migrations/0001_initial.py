# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 21:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=150, null=True, verbose_name='username')),
                ('message', models.TextField(blank=True, default=None, null=True)),
                ('stack_trace', models.TextField(blank=True, default=None, null=True)),
                ('type_error', models.TextField(blank=True, default=None, null=True)),
                ('log_level', models.CharField(default='ERROR', max_length=10, verbose_name='Log level')),
                ('environment', models.TextField(blank=True, default=None, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('notes', models.TextField(blank=True, default=None, null=True)),
            ],
        ),
    ]
