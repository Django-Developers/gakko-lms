import os
import datetime
from django.db import models
from django.core.validators import MaxValueValidator
from django.db.models import constraints
from django.db.models.fields import related
from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext as _
# from django.contrib.auth import get_user_model

from user.models import User

# TO-do units of each course can't be more than 5


class Course(models.Model):
    # number = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    detail = models.CharField(_("What is this ???"),
                              max_length=200, default=' ')
    faculty = models.CharField(_("faculty name"), max_length=200)  # daneshkade
    unit_count = models.PositiveIntegerField(
        _("Unit"), validators=[MaxValueValidator(5)])

    def __str__(self):
        return f'{self.title} - {self.faculty}'

class CourseResources(models.Model):
    title = models.CharField(max_length=50)
    file_url = models.FileField(upload_to='courseResources')
    course = models.ForeignKey(Course,on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("CourseResources")
        verbose_name_plural = _("CourseResourcess")

    def __str__(self):
        return self.title



'''
This part is for user model but don't want to mess with nilu's work :( 
'''


class RegisterdCourses(models.Model):
    user = models.ForeignKey(User, verbose_name=_(""),
                             on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, verbose_name=_(""), on_delete=models.CASCADE)


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

    time_start = models.TimeField(_("Class Startes"), blank=True, null=True)
    time_finish = models.TimeField(_("Class Finishes"), blank=True, null=True)

    date = models.DateField(_("Date"), blank=True, null=True)

    def __str__(self):
        return f'{self.course.title} - {self.day_of_week}'


# To-do upload to needs rework (function instead of directory)
# /ashkan/django <-  File
# /ashkan/django/asnwers <- Answers
class HomeWork(models.Model):
    title = models.CharField(max_length=100)
    send_time = models.DateTimeField(auto_now_add=True)
    deadline = models.DateTimeField(null=True, blank=True)
    attachment = models.FileField(
        _("HomeWorkFile"), upload_to='homeworks', max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey(User, on_delete=models.RESTRICT)
    weight = models.PositiveIntegerField(default=1)

    @property
    def remaining_days(self):
        return self.deadline.replace(tzinfo=None) - datetime.datetime.now()
    
    @property 
    def passed_sending_time(self):
        if self.remaining_days.total_seconds() < 0:
            return True
        else:
            return False
            
    class Meta:
        ordering = ['-send_time', 'deadline', 'title']

    def __str__(self):
        return f'{self.title} - {self.deadline.replace(tzinfo=None) - datetime.datetime.now()}'


def get_upload_path(instance, filename):
    pass
    # return os.path.join(f"{instance.}", filename)


class HomeWorkAnswer(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    home_work = models.ForeignKey(HomeWork, on_delete=models.CASCADE)
    answer_file = models.FileField(
        upload_to='Hanswer', null=True, blank=True)
    answer_text = models.TextField(_("Explain The answer"))
    delivery_time = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(
        _("When Answer Was Changed"), auto_now=True)
    student_score = models.FloatField(null=True, blank=True, max_length=20)

    def __str__(self):
        return f'{self.student.username} - {self.home_work.title} - {self.delivery_time}'

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

    class Meta:
        ordering = ['-start_time', 'end_time', 'title']

    def __str__(self):
        return f' {self.title} - {self.start_time} - {self.end_time}'


class QuizQuestion(models.Model):
    title = models.CharField(max_length=255)
    attachment = models.FileField(null=True, blank=True)  # peyvast
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

    def __str__(self):
        return f' {self.title} - Quiz :{self.quiz.title}'


class QuestionAnswer(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    answer = models.FileField(
        upload_to='Qanswers', null=True, blank=True)
    student_score = models.FloatField(null=True, blank=True, max_length=20)


'''
There can be general purpose or course specefic !!! 
Therfore null on course fk.
'''


class BulletinBoard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    publisher = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(
        Course, on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.title} , by {self.publisher.username}'
