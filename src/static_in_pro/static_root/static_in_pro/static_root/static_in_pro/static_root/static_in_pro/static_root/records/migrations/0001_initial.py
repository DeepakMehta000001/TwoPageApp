# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Add',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(default='', max_length=20)),
                ('age', models.SmallIntegerField()),
                ('dob', models.DateField()),
            ],
        ),
    ]
