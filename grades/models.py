# from django.db import models
# from django.db.models import constraints
# from django.utils.translation import gettext as _

# from user.models import User
# from education.models import Course,HomeWork,HomeWorkAnswer

# '''

# '''

# class HomeWorkAnswerMark(models.Model):
    
#     '''
#     A mark For each lesson student have
#     '''
#     # student = models.ForeignKey(Student, verbose_name=_(""), on_delete=models.CASCADE)
#     # lesson = models.ForeignKey(Course, verbose_name=_(""), on_delete=models.CASCADE)
#     HomeWorkAnswer = models.ForeignKey(HomeWorkAnswer, verbose_name=_(""), on_delete=models.CASCADE) 
#     teacher = models.ForeignKey(User, verbose_name=_(""), on_delete=models.CASCADE)
#     mark = models.FloatField(_("Student Mark in HomeWork"))
    
#     class Meta:
#         verbose_name = _("studentmark")
#         verbose_name_plural = _("studentsmark")
#         constraints = [
#             constraints.UniqueConstraint(name='student-lesson',fields=['student','lesson'])
#         ]
        
#     def __str__(self):
#         return f'{self.student} - {self.lesson} => {self.mark}'

# class CourseStudentMark(models.Model):
    
#     '''
#     Each Student has a mark in each exercise done in lesson
#     '''

#     # student = models.ForeignKey(Student, verbose_name=_(""), on_delete=models.CASCADE)
#     # lesson = models.ForeignKey(Course, verbose_name=_(""), on_delete=models.CASCADE)
#     # exercise = models.ForeignKey(HomeWork, verbose_name=_(""), on_delete=models.CASCADE)
    
#     mark = models.FloatField(_("Student Mark in exrecise"))
    
#     class Meta:
#         verbose_name = _("studentmark")
#         verbose_name_plural = _("studentsmark")
#         constraints = [
#             constraints.UniqueConstraint(name='student-lesson',fields=['student','lesson'])
#         ]
        
#     def __str__(self):
#         return f'{self.student} - {self.lesson} => {self.mark}'
