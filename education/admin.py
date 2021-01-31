import builtins
from django.contrib import admin
from nested_inline.admin import NestedStackedInline, NestedModelAdmin

from .models import (Quiz, QuizQuestion, QuestionAnswer, HomeWork,
                     HomeWorkAnswer, BulletinBoard, Course, CourseSession, RegisterdCourses, CourseResources)


class QuizQuestionAnswersInline(NestedStackedInline):
    model = QuestionAnswer
    extra = 1
    fk_name = 'question'


class QuizQuestionInline(NestedStackedInline):
    model = QuizQuestion
    extra = 1
    fk_name = 'quiz'
    inlines = [QuizQuestionAnswersInline]


class QuizInline(NestedStackedInline):
    model = Quiz
    extra = 1
    fk_name = 'course'
    inlines = [QuizQuestionInline]


class HomeWorkAwnsersInline(NestedStackedInline):
    model = HomeWorkAnswer
    extra = 1
    fk_name = 'home_work'


class HomeWorkInline(NestedStackedInline):
    model = HomeWork
    extra = 1
    fk_name = 'course'
    inlines = [HomeWorkAwnsersInline]


class CourseSessionInline(NestedStackedInline):
    model = CourseSession
    extra = 1
    fk_name = 'course'


class StudentsInline(NestedStackedInline):
    model = RegisterdCourses
    extra = 1
    fk_name = 'course'


class ResourcesInline(NestedStackedInline):
    model = CourseResources
    extra = 1
    fk_name = 'course'


class BulletinBoardInline(NestedStackedInline):
    model = BulletinBoard
    extra = 1
    fk_name = 'course'


class TopLevelAdmin(NestedModelAdmin):
    model = Course
    inlines = [QuizInline, HomeWorkInline, CourseSessionInline, StudentsInline,ResourcesInline,BulletinBoardInline]


admin.site.register(Course, TopLevelAdmin)
admin.site.register(BulletinBoard)
