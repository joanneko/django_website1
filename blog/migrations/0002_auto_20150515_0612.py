# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_on',
            new_name='created',
        ),
        migrations.RemoveField(
            model_name='post',
            name='category',
        ),
        migrations.RemoveField(
            model_name='post',
            name='last_modified',
        ),
        migrations.AddField(
            model_name='post',
            name='description',
            field=models.CharField(default=datetime.datetime(2015, 5, 15, 6, 12, 29, 521255, tzinfo=utc), max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(default='', unique=True, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
