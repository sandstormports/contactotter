# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-20 03:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0003_auto_20150904_2018'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='last_contact',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='logentry',
            name='kind',
            field=models.CharField(blank=True, choices=[('twitter', 'Twitter'), ('tumblr', 'Tumblr'), ('facebook', 'Facebook'), ('email', 'Email'), ('in person', 'In Person'), ('website', 'Website'), ('other', 'Other'), ('edit', 'Edit')], max_length=100, null=True),
        ),
    ]
