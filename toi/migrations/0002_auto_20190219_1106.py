# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-19 11:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('toi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Level2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Level3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menu', models.CharField(max_length=60)),
                ('newmenu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toi.Level2')),
            ],
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='Level1',
        ),
        migrations.AddField(
            model_name='level2',
            name='submenu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='toi.Level1'),
        ),
    ]
