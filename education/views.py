from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView,DetailView
from django.views import View

from .models import *
from .models import RegisterdCourses


class ClassesMixIn():
    _model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # context["classes"] = self.model.objects.all()

        # self.classes = RegisterdCourses.objects.all()
        self.classes = RegisterdCourses.objects.filter(user=self.request.user)
        print(self.classes)
        context["classes"] = self.classes
        return context


'''
Here I need to prefetch_related from User__course__homework__homeworkAnwsers
'''


class HomeWorkMixIn():
    _model = HomeWork

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # quiz.objects.filter(course__u__name__icontains = 'N')
        context["Homewoks"] = HomeWork.objects.none()

        return context


class HomeWorkAnswerMixIn():
    _model = HomeWork

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # quiz.objects.filter(course__u__name__icontains = 'N')
        context["HomewoksAnswer"] = HomeWorkAnswer.objects.none()
        return context


class Dashboard(ClassesMixIn,LoginRequiredMixin,TemplateView):
    template_name = 'dashboard.html'


class CourseDetailView(DetailView):
    model = Course
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context["courseresources"] = CourseResources.objects.filter(course = self.object)
        context["coursesession"] = CourseSession.objects.filter(course = self.object)
        context["bulletinboard"] = BulletinBoard.objects.filter(course=self.object)
        print(context)
        return context
    
    # template_name = "course/course-detail.html"
    
class CourseListView(ListView):
    model = Course
