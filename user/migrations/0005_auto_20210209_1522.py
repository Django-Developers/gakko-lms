# Generated by Django 3.1.5 on 2021-02-09 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('education', '0008_auto_20210204_1546'),
        ('user', '0004_auto_20210209_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='course',
            field=models.ManyToManyField(blank=True, to='education.Course'),
        ),
    ]
