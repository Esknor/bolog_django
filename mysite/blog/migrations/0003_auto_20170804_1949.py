# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2017-08-04 16:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170803_0252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='coments_article',
            new_name='comments_article',
        ),
    ]
