# Generated by Django 3.1.5 on 2021-01-31 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('education', '0003_auto_20210130_1909'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='homework',
            options={'ordering': ['send_time', 'deadline', 'title']},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ['start_time', 'end_time', 'title']},
        ),
        migrations.AddField(
            model_name='course',
            name='detail',
            field=models.CharField(default=' ', max_length=200, verbose_name='What is this ???'),
        ),
        migrations.CreateModel(
            name='RegisterdCourses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.course', verbose_name='')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='')),
            ],
        ),
    ]