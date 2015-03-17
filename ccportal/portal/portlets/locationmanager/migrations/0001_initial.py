# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('image', models.ImageField(height_field=10, width_field=100, upload_to=b'')),
                ('title', models.CharField(max_length=255)),
                ('coordinates', models.CharField(max_length=31)),
                ('description', models.TextField()),
                ('author', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.IntegerField(unique=True, serialize=False, primary_key=True)),
                ('description', models.TextField()),
                ('photo', models.ImageField(height_field=10, width_field=100, upload_to=b'')),
                ('location', models.ForeignKey(to='locationmanager.Location')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
