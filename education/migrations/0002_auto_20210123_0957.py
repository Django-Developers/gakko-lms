# Generated by Django 3.1.5 on 2021-01-23 09:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('education', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='questionanswer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='homeworkanswer',
            name='home_work',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.homework'),
        ),
        migrations.AddField(
            model_name='homeworkanswer',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='homework',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.course'),
        ),
        migrations.AddField(
            model_name='homework',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='coursesession',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.course'),
        ),
        migrations.AddField(
            model_name='bulletinboard',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='quizquestion',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.quiz'),
        ),
        migrations.AddConstraint(
            model_name='homeworkanswer',
            constraint=models.UniqueConstraint(fields=('student', 'home_work'), name='homeworkanwser'),
        ),
    ]
