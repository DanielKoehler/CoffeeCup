# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('locationmanager', '0002_auto_20150316_1342'),
    ]

    operations = [
        migrations.RenameField(
            model_name='location',
            old_name='longditude',
            new_name='longitude',
        ),
    ]
