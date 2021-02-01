from django.shortcuts import redirect, render,get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, TemplateView, DetailView
from django.core.files.storage import FileSystemStorage

from .models import *
from .models import RegisterdCourses

from .forms import HomeWorkAnswerForm


class ClassesMixIn():
    _model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        self.classes = RegisterdCourses.objects.select_related(
            'course').filter(user=self.request.user)
        context["classes"] = self.classes
        return context


'''
Here I need to prefetch_related from User__course__homework__homeworkAnwsers
'''


class HomeWorkMixIn():
    _model = HomeWork

    '''
    Only works if it's a detail view(needs self.object)
    And self.object is an instance of Course model
    '''

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if hasattr(self, 'classes'):
            context["homeworks"] = []
            for _class in self.classes:
                context["homeworks"].append(
                    {'homeworks': _class.course.homework_set.all(), 'course_title': _class.course.title})

        else:
            if isinstance(self.object, Course):
                homeworks = list(HomeWork.objects.filter(
                    course=self.object))
                for hw in homeworks:
                    homeworks.remove(hw)
                    homeworks.append({'homework': hw,
                                      'answer': hw.homeworkanswer_set.filter(student_id=self.request.user)
                                      })

                context["homeworks"] = homeworks

            else:
                context["homeworks"] = HomeWork.objects.none()
        return context

    def post(self, request, *args, **kwargs):

        # form = HomeWorkAnswerForm(data=request.POST, files=request.FILES)
        home_work_obj = get_object_or_404(HomeWork,id = request.POST['home_work'])
        answer_obj =  HomeWorkAnswer.objects.get(student = request.user,
                                   home_work = home_work_obj)
        if not answer_obj:
            HomeWorkAnswer(student=request.user,
                       home_work=home_work_obj,
                       answer_file=FileSystemStorage().save(
                           f"{HomeWorkAnswer.answer_file.field.upload_to}/{request.FILES['answer_file'].name}", request.FILES['answer_file']),
                       answer_text = request.POST['answer_text'],
                       ).save()
        else:
            answer_obj.answer_file = FileSystemStorage().save(
                           f"{HomeWorkAnswer.answer_file.field.upload_to}/{request.FILES['answer_file'].name}", request.FILES['answer_file'])
            answer_obj.answer_text = request.POST['answer_text']
            answer_obj.save()
            
        

        if hasattr(super(), 'post'):
            return super().post(request, args, kwargs)
        return redirect(request.build_absolute_uri())


# class HomeWorkAnswerMixIn():
#     _model = HomeWork

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # quiz.objects.filter(course__u__name__icontains = 'N')
#         context[""] = HomeWorkAnswer.objects.none()
#         return context


class Dashboard(HomeWorkMixIn, ClassesMixIn, LoginRequiredMixin, TemplateView):
    template_name = 'dashboard.html'


class CourseDetailView(HomeWorkMixIn, DetailView):
    model = Course

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context["courseresources"] = CourseResources.objects.filter(
            course=self.object)
        context["coursesession"] = CourseSession.objects.filter(
            course=self.object)
        context["bulletinboard"] = BulletinBoard.objects.filter(
            course=self.object)

        return context


class CourseListView(ListView):
    model = Course


class BulletinBoardListView(ListView):
    model = BulletinBoard
    # template_name = ".html"


class BulletinBoardDetailView(DetailView):
    model = BulletinBoard
