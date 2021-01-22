from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager


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
    
    #username=models.CharField(max_length=150,unique=True)
    #email=models.EmailField(max_length=255,unique=True)
    #full_name=models.CharField(max_length=150,unique=True)
    #first_name=models.CharField(max_length=150,unique=True)
    university_id=models.CharField(max_length=255,primary_key=True)
    user_choices=(
        ('student','student'),
        ('teacher','teacher'),
        ('university_staff','university_staff'),
    )
    user_type=models.CharField(max_length=155,choices=user_choices)

    active= models.BooleanField(default=True) #can login
    #staff=models.BooleanField(default=False) #staff user non superuser
    #admin=models.BooleanField(default=False) #superuser

    USERNAME_FIELD = 'email'
    #USERNAME_FIELD and password are required by default

    REQUIRED_FIELDS=[] #python manage.py createsuperuser

    def __str__(self):
        return self.university_id
#for absent/present
class AP(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    course=models.ForeignKey(Course_session,on_delete=models.CASCADE)



class profile(models.Model):
    user= models.OneToOneField(User,on_delete=models.CASCADE)
