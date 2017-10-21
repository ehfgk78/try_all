# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 05:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('models_doc', '0005_auto_20171021_1323'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('debut_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Idol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('joined_date', models.DateField(blank=True, null=True)),
                ('is_active', models.BooleanField()),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='models_doc.Group')),
                ('idol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membership_set', to='models_doc.Idol')),
                ('recommender', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recommend_membership_set', to='models_doc.Idol')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='members',
            field=models.ManyToManyField(through='models_doc.Membership', to='models_doc.Idol'),
        ),
    ]