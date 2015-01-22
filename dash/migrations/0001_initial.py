# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('date_assigned', models.DateField(null=True, blank=True)),
                ('date_due', models.DateField(null=True, blank=True)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('title',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='AssignmentPupilRelationship',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('grade', models.CharField(null=True, blank=True, max_length=3)),
                ('date_submitted', models.DateField(null=True, blank=True)),
                ('assignment', models.ForeignKey(to='dash.Assignment')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Pupil',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('dob', models.DateField(blank=True)),
                ('number', models.CharField(blank=True, max_length=50)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('last_name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(blank=True, max_length=75)),
                ('slug', models.SlugField()),
            ],
            options={
                'ordering': ('last_name',),
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeacherSubjectRelationship',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('level', models.CharField(choices=[('Credit', 'Credit'), ('General', 'General'), ('Foundation', 'Foundation')], max_length=30)),
                ('subject', models.ForeignKey(to='dash.Subject')),
                ('teacher', models.ForeignKey(to='dash.Teacher')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='teacher',
            name='subjects',
            field=models.ManyToManyField(to='dash.Subject', through='dash.TeacherSubjectRelationship'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignmentpupilrelationship',
            name='pupil',
            field=models.ForeignKey(to='dash.Pupil'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(to='dash.TeacherSubjectRelationship'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='assignment',
            name='pupils',
            field=models.ManyToManyField(to='dash.Pupil', through='dash.AssignmentPupilRelationship'),
            preserve_default=True,
        ),
    ]
