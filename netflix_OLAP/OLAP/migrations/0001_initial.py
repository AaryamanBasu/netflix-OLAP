# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-09 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CompletionRate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_Name', models.CharField(max_length=255)),
                ('show_Director', models.CharField(max_length=255)),
                ('show_Name', models.CharField(max_length=255)),
                ('show_id', models.IntegerField()),
                ('runtime', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='FavDirector',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_Name', models.CharField(max_length=255)),
                ('director_id', models.CharField(max_length=255)),
                ('director_Name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PlanRecommender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_Name', models.CharField(max_length=255)),
                ('user_Age', models.IntegerField()),
                ('plan_Name', models.CharField(max_length=255)),
                ('plan_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='showBudgetRecommender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_Name', models.CharField(max_length=255)),
                ('show_id', models.IntegerField()),
                ('show_Name', models.CharField(max_length=255)),
                ('budget_Amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShowRecommender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('user_Name', models.CharField(max_length=255)),
                ('show_Name', models.CharField(max_length=255)),
                ('show_id', models.IntegerField()),
                ('genre_id', models.IntegerField()),
                ('genre_Type', models.CharField(max_length=255)),
            ],
        ),
    ]
