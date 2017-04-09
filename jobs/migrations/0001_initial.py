# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-09 05:35
from __future__ import unicode_literals

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=140)),
                ('description', models.TextField(default='')),
                ('zipcode', models.CharField(default='', max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('due_date', models.CharField(default='', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='job',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]
