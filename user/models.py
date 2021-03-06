from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import AbstractUser, UserManager
# from education.models import CourseSession


class Student(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='S')


class Teacher(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='T')


class University_staff(UserManager):
    def get_queryset(self):
        return super().get_queryset().filter(user_type='U')

class NewUserManager(UserManager):
    def create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("user must have email address")
        user =self.model(
            email=self.normalize_email,
            password=password
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractUser):
  
    # @property
    # def is_teacher(self):
    #     if self.user_type=='T':
    #         return True
    #     else:
    #         return False
 
    

    # username=models.CharField(max_length=150,unique=True)
    # email=models.EmailField(max_length=255,unique=True)
    # full_name=models.CharField(max_length=150,unique=True)
    # first_name=models.CharField(max_length=150,unique=True)
    # last_login=models.DateTimeField(verbose_name='last login', auto_now=True)
    #university_id = models.CharField(max_length=255, primary_key=True, auto_created=True)
    university_id = models.AutoField(primary_key=True,auto_created=True)
    course=models.ManyToManyField("education.Course",blank=True)

    user_choices = (
        ('S','student'),
        ('T','teacher' ),
        ('U', 'university_staff'),
    )
    user_type = models.CharField(max_length=2, choices=user_choices,default='S')

    # active= models.BooleanField(default=True) #can login
    # staff=models.BooleanField(default=False) #staff user non superuser
    # admin=models.BooleanField(default=False) #superuser

    #USERNAME_FIELD = 'email'
    # USERNAME_FIELD and password are required by default
    objects = UserManager()
    students = Student()
    teachers = Teacher()
    uni = University_staff()
    # REQUIRED_FIELDS=['email'] #python manage.py createsuperuser
    #def has_perm(self,perm,obj=None):
        #return self.is_admin

    #def has_module_perms(self,app_label):
        #return self.is_admin
        
    # def save(self,*args, **kwargs):
    #     if not self.user_type :
    #         self.user_type = 'S'
    #     return super().save(args,kwargs)

    def __str__(self):
        return str(self.university_id)


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