import os
from django.db import models
from django.db.models import constraints
from django.utils.translation import gettext as _
# from django.contrib.auth import get_user_model

from user.models import User

    # TO-do units of each course can't be more than 5
class Course(models.Model):
    # number = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    field = models.CharField(max_length=200)  # daneshkade
    unit_count = models.IntegerField(_("Unit"))


class CourseSession(models.Model):

    WEEK_DAYS = (
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
        ('mon', 'Monday'),
        ('tues', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thur', 'Thursday'),
        ('fri', 'Friday'),
    )

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    day_of_week = models.CharField(
        _("Day of the week"), max_length=4, choices=WEEK_DAYS)
    time = models.TimeField(_("Class Time"))


# To-do upload to needs rework (function instead of directory)
class HomeWork(models.Model):
    title = models.CharField(max_length=100)
    send_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(
        _("HomeWorkFile"), upload_to='homeworks', max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.RESTRICT)
    weight = models.PositiveIntegerField(default=1)


def get_upload_path(instance, filename):
    pass
    # return os.path.join(f"{instance.}", filename)


class HomeWorkAnswer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    home_work = models.ForeignKey(HomeWork, on_delete=models.CASCADE)
    answer_file = models.FileField(
        upload_to=get_upload_path, null=True, blank=True)
    answer_text = models.TextField(_("Explain The answer"))
    delivery_time = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(
        _("When Answer Was Changed"), auto_now=True)
    student_score = models.FloatField(null=True, blank=True, max_length=20)

    class Meta:
        constraints = [
            constraints.UniqueConstraint(
                name='homeworkanwser', fields=['student', 'home_work'])
        ]


class Quiz(HomeWork):
    send_time = None
    deadline = None
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()


class QuizQuestion(models.Model):
    title = models.CharField(max_length=255)
    attachment = models.FileField(null=True, blank=True)  # peyvast
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)


class QuestionAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.FileField(
        upload_to=get_upload_path, null=True, blank=True)
    student_score = models.FloatField(null=True, blank=True, max_length=20)


class BulletinBoard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)


