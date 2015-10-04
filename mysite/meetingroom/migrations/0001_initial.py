# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('creater', models.CharField(max_length=40)),
                ('team', models.CharField(max_length=20)),
                ('teamId', models.CharField(max_length=20)),
                ('roomName', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=40)),
                ('issue', models.CharField(max_length=40)),
                ('meetingType', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=20)),
                ('start_time', models.CharField(max_length=20)),
                ('end_time', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingRoom',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('roomName', models.CharField(max_length=20)),
                ('roomNameId', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('firstName', models.CharField(max_length=40)),
                ('lastName', models.CharField(max_length=20)),
                ('nickName', models.CharField(max_length=20)),
                ('e_mail', models.CharField(max_length=40)),
                ('team', models.CharField(max_length=20)),
                ('teamId', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MembersJoin',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('e_mail', models.CharField(max_length=40)),
                ('meeting', models.ForeignKey(to='meetingroom.Meeting')),
            ],
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('teamName', models.CharField(max_length=20)),
                ('teamId', models.CharField(max_length=20)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
