# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0004_remove_record_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='position',
            new_name='location',
        ),
    ]
