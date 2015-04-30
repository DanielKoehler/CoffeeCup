# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediasharing', '0002_directory_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='directory',
        ),
        migrations.AddField(
            model_name='directory',
            name='parent',
            field=models.ForeignKey(to='mediasharing.Directory', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='file',
            name='parent',
            field=models.ForeignKey(to='mediasharing.Directory', null=True),
            preserve_default=True,
        ),
    ]
