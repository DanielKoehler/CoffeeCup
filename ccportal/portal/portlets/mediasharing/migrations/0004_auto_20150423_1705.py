# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediasharing', '0003_auto_20150423_1651'),
    ]

    operations = [
        migrations.AddField(
            model_name='directory',
            name='bytes',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='directory',
            name='parent',
            field=models.ForeignKey(blank=True, to='mediasharing.Directory', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='file',
            name='parent',
            field=models.ForeignKey(blank=True, to='mediasharing.Directory', null=True),
            preserve_default=True,
        ),
    ]
