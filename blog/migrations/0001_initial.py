# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('text', models.TextField()),
                ('posts_count', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
