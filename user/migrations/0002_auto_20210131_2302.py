# Generated by Django 3.1.5 on 2021-01-31 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='university_id',
            field=models.CharField(auto_created=True, max_length=255, primary_key=True, serialize=False),
        ),
    ]
