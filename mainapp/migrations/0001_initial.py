# Generated by Django 3.2.13 on 2022-07-17 09:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=50)),
                ('project_link', models.URLField()),
                ('project_dp', models.ImageField(upload_to='')),
                ('project_description', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('userName', models.CharField(max_length=30)),
                ('mobileNum', models.CharField(max_length=12)),
                ('question', models.CharField(max_length=200)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 17, 2, 14, 59, 517777))),
            ],
        ),
    ]