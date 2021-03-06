# Generated by Django 3.1.5 on 2021-01-23 09:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BulletinBoard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('field', models.CharField(max_length=200)),
                ('unit_count', models.IntegerField(verbose_name='Unit')),
            ],
        ),
        migrations.CreateModel(
            name='CourseSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day_of_week', models.CharField(choices=[('sat', 'Saturday'), ('sun', 'Sunday'), ('mon', 'Monday'), ('tues', 'Tuesday'), ('wed', 'Wednesday'), ('thur', 'Thursday'), ('fri', 'Friday')], max_length=4, verbose_name='Day of the week')),
                ('time_start', models.TimeField(verbose_name='Class Startes')),
                ('time_finish', models.TimeField(verbose_name='Class Finishes')),
            ],
        ),
        migrations.CreateModel(
            name='HomeWork',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('send_time', models.DateTimeField(auto_now_add=True)),
                ('deadline', models.DateTimeField(blank=True, null=True)),
                ('attachment', models.FileField(upload_to='homeworks', verbose_name='HomeWorkFile')),
                ('weight', models.PositiveIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='HomeWorkAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_file', models.FileField(blank=True, null=True, upload_to='Hanswer')),
                ('answer_text', models.TextField(verbose_name='Explain The answer')),
                ('delivery_time', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='When Answer Was Changed')),
                ('student_score', models.FloatField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('attachment', models.FileField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('homework_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='education.homework')),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
            bases=('education.homework',),
        ),
        migrations.CreateModel(
            name='QuestionAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.FileField(blank=True, null=True, upload_to='Qanswers')),
                ('student_score', models.FloatField(blank=True, max_length=20, null=True)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='education.quizquestion')),
            ],
        ),
    ]
