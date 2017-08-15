# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-08-12 09:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(max_length=450)),
                ('preference', models.CharField(max_length=90)),
            ],
            options={
                'db_table': 'answer',
            },
        ),
        migrations.CreateModel(
            name='Aspiration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('industry', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'aspiration',
            },
        ),
        migrations.CreateModel(
            name='AspirationSkillMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference', models.CharField(max_length=100)),
                ('aspiration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_data.Aspiration')),
            ],
            options={
                'db_table': 'skill_aspiration',
            },
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'task_question',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('type', models.CharField(blank=True, choices=[('LONGLIST', 'LONGLIST'), ('TXTARR3', 'TXTARR3'), ('TXTMCQ2', 'TXTMCQ2'), ('DP', 'DP'), ('TC', 'TC'), ('LSK', 'LSK'), ('TXTMCQ5', 'TXTMCQ5'), ('TXTMCQ4', 'TXTMCQ4'), ('TXTMCQ3', 'TXTMCQ3'), ('TXT', 'TXT')], max_length=150, null=True)),
                ('created_by', models.CharField(blank=True, default='system', max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'question',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'skill',
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('question', models.ManyToManyField(through='add_data.Membership', to='add_data.Question')),
            ],
            options={
                'db_table': 'task',
            },
        ),
        migrations.CreateModel(
            name='TaskAspirationMapping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preference', models.CharField(max_length=100)),
                ('aspiration', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_data.Aspiration')),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_data.Task')),
            ],
            options={
                'db_table': 'aspiration_task',
            },
        ),
        migrations.AddField(
            model_name='membership',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_data.Question'),
        ),
        migrations.AddField(
            model_name='membership',
            name='task',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_data.Task'),
        ),
        migrations.AddField(
            model_name='aspirationskillmapping',
            name='skill',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_data.Skill'),
        ),
        migrations.AddField(
            model_name='aspiration',
            name='task',
            field=models.ManyToManyField(through='add_data.TaskAspirationMapping', to='add_data.Task'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_data.Question'),
        ),
    ]
