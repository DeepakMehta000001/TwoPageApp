# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0003_auto_20161216_2048'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='name',
        ),
    ]
