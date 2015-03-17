# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('site', '0002_user_user_role'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='user_role',
            new_name='role',
        ),
    ]
