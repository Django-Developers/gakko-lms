import builtins
from django.contrib import admin
from nested_inline.admin import NestedTabularInline, NestedModelAdmin

from .models import (Quiz, QuizQuestion, QuestionAnswer, HomeWork,
                     HomeWorkAnswer, BulletinBoard, Course, CourseSession, RegisterdCourses, CourseResources)


class QuizQuestionAnswersInline(NestedTabularInline):
    model = QuestionAnswer
    extra = 1
    fk_name = 'question'


class QuizQuestionInline(NestedTabularInline):
    model = QuizQuestion
    extra = 1
    fk_name = 'quiz'
    inlines = [QuizQuestionAnswersInline]


class QuizInline(NestedTabularInline):
    model = Quiz
    extra = 1
    fk_name = 'course'
    inlines = [QuizQuestionInline]


class HomeWorkAwnsersInline(NestedTabularInline):
    model = HomeWorkAnswer
    extra = 1
    fk_name = 'home_work'


class HomeWorkInline(NestedTabularInline):
    model = HomeWork
    extra = 1
    fk_name = 'course'
    inlines = [HomeWorkAwnsersInline]


class CourseSessionInline(NestedTabularInline):
    model = CourseSession
    extra = 1
    fk_name = 'course'


class StudentsInline(NestedTabularInline):
    model = RegisterdCourses
    extra = 1
    fk_name = 'course'


class ResourcesInline(NestedTabularInline):
    model = CourseResources
    extra = 1
    fk_name = 'course'


class BulletinBoardInline(NestedTabularInline):
    model = BulletinBoard
    extra = 1
    fk_name = 'course'


class TopLevelAdmin(NestedModelAdmin):
    model = Course
    inlines = [QuizInline, HomeWorkInline, CourseSessionInline, StudentsInline,ResourcesInline,BulletinBoardInline]


admin.site.register(Course, TopLevelAdmin)
admin.site.register(BulletinBoard)
