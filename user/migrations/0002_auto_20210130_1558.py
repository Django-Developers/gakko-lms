# Generated by Django 3.1.5 on 2021-01-30 15:58

import django.contrib.auth.models
from django.db import migrations
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('students', user.models.Student()),
                ('teachers', user.models.Teacher()),
                ('uni', user.models.University_staff()),
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
