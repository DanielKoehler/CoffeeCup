# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mediasharing', '0004_auto_20150423_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='mime',
            field=models.CharField(max_length=64, null=True, blank=True),
            preserve_default=True,
        ),
    ]
