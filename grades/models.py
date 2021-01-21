from django.db import models
from django.db.models import constraints
from django.utils.translation import gettext as _

from user.models import Student
from education.models import Lesson,Exercise

'''

'''

class StudentMark(models.Model):
    
    '''
    A mark For each lesson student have
    '''

    student = models.ForeignKey(Student, verbose_name=_(""), on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name=_(""), on_delete=models.CASCADE)
    mark = models.IntegerField(_("Student Mark in lesson"))
    
    class Meta:
        verbose_name = _("studentmark")
        verbose_name_plural = _("studentsmark")
        constraints = [
            constraints.UniqueConstraint(name='student-lesson',fields=['student','lesson'])
        ]
        
    def __str__(self):
        return f'{self.student} - {self.lesson} => {self.mark}'

class ExerciseMark(models.Model):
    
    '''
    Each Student has a mark in each exercise done in lesson
    '''

    student = models.ForeignKey(Student, verbose_name=_(""), on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, verbose_name=_(""), on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, verbose_name=_(""), on_delete=models.CASCADE)
    mark = models.IntegerField(_("Student Mark in lesson"))
    
    class Meta:
        verbose_name = _("studentmark")
        verbose_name_plural = _("studentsmark")
        constraints = [
            constraints.UniqueConstraint(name='student-lesson',fields=['student','lesson'])
        ]
        
    def __str__(self):
        return f'{self.student} - {self.lesson} => {self.mark}'
