# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0006_record_place'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='record',
            name='place',
        ),
    ]
