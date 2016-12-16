# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('first_name', models.CharField(max_length=20, default='')),
                ('last_name', models.CharField(max_length=20, default='')),
                ('email', models.EmailField(max_length=254)),
                ('mobile', models.CharField(max_length=20, default='')),
                ('age', models.PositiveIntegerField()),
                ('dob', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='Add',
        ),
    ]
