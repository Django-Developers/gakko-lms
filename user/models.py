from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser, UserManager
# from education.models import CourseSession


class Student(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='student')


class Teacher(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='teacher')


class University_staff(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='university_staff')


class User(AbstractUser):

    # username=models.CharField(max_length=150,unique=True)
    # email=models.EmailField(max_length=255,unique=True)
    # full_name=models.CharField(max_length=150,unique=True)
    # first_name=models.CharField(max_length=150,unique=True)
    university_id = models.CharField(max_length=255,auto_created=True, primary_key=True)
    user_choices = (
        ('S', 'student'),
        ('T', 'teacher'),
        ('U', 'university_staff'),
    )
    user_type = models.CharField(max_length=1, choices=user_choices)

    # active= models.BooleanField(default=True) #can login
    # staff=models.BooleanField(default=False) #staff user non superuser
    # admin=models.BooleanField(default=False) #superuser

    # USERNAME_FIELD = 'email'
    # USERNAME_FIELD and password are required by default
    objects = UserManager()
    students = Student()
    teachers = Teacher()
    uni = University_staff()
    # REQUIRED_FIELDS=['email'] #python manage.py createsuperuser

    def __str__(self):
        return self.university_id


class profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return User.university_id


# for absent/present
class AP(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_session = models.ForeignKey(
        'education.CourseSession', on_delete=models.CASCADE)
    when = models.DateField(_("When was he/she present"), auto_now_add=True)