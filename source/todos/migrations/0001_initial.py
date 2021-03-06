# Generated by Django 3.0.5 on 2020-06-04 09:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=1000)),
                ('isComplete', models.BooleanField(default=False)),
                ('date_created', models.DateField(default=datetime.date)),
                ('time_created', models.TimeField(default=datetime.time)),
            ],
        ),
    ]
