# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import geoposition.fields


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0002_auto_20161216_1554'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='name',
            field=models.CharField(default='default', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='record',
            name='position',
            field=geoposition.fields.GeopositionField(default=1, max_length=42),
            preserve_default=False,
        ),
    ]
