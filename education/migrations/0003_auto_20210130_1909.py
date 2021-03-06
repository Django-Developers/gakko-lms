# Generated by Django 3.1.5 on 2021-01-30 19:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0002_auto_20210123_0957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='field',
        ),
        migrations.AddField(
            model_name='course',
            name='faculty',
            field=models.CharField(default=1, max_length=200, verbose_name='faculty name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coursesession',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='course',
            name='unit_count',
            field=models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(5)], verbose_name='Unit'),
        ),
        migrations.AlterField(
            model_name='coursesession',
            name='time_finish',
            field=models.TimeField(blank=True, null=True, verbose_name='Class Finishes'),
        ),
        migrations.AlterField(
            model_name='coursesession',
            name='time_start',
            field=models.TimeField(blank=True, null=True, verbose_name='Class Startes'),
        ),
    ]
