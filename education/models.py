from django.db import models
import os


class Course(models.Model):
    # number = models.PositiveIntegerField(primary_key=True)
    title = models.CharField(max_length=200)
    field = models.CharField(max_length=200)  # daneshkade


class HomeWork(models.Model):
    title = models.CharField(max_length=100)
    send_time = models.DateTimeField()
    deadline = models.DateTimeField()

    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey('User', on_delete=models.RESTRICT)
    score = models.PositiveIntegerField()


def get_upload_path(instance, filename):
    pass
    # return os.path.join(f"{instance.}", filename)


class HomeWorkAnswer(models.Model):
    home_work = models.ForeignKey(HomeWork, on_delete=models.CASCADE)
    student = models.ForeignKey('User', on_delete=models.CASCADE)
    answer = models.FileField(
        upload_to=get_upload_path, null=True, blank=True)
    delivery_time = models.DateTimeField()
    student_score = models.PositiveIntegerField(null=True, blank=True)


class BulletinBoard(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=255)
    publisher = models.ForeignKey('User', on_delete=models.CASCADE)


class Quiz(models.Model):
    title = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    teacher = models.ForeignKey('User', on_delete=models.RESTRICT)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    score = models.PositiveIntegerField()


class Question(models.Model):
    title = models.CharField(max_length=255)
    ps = models.FileField(null=True, blank=True)  # peyvast
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.PositiveIntegerField()


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    student = models.ForeignKey('User', on_delete=models.CASCADE)
    answer = models.FileField(
        upload_to=get_upload_path, null=True, blank=True)
    student_score = models.PositiveIntegerField(null=True, blank=True)
