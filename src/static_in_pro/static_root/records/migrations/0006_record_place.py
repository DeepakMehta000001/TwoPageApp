# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0005_auto_20161216_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='place',
            field=models.CharField(default='', max_length=50),
        ),
    ]
