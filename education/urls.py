from django.urls import path

from .views import Dashboard,CourseDetailView,CourseListView,BulletinBoardListView,BulletinBoardDetailView

urlpatterns = [
    path('dash/', Dashboard.as_view(), name='dashboard'),
    path('course/<int:pk>', CourseDetailView.as_view(), name='course-detail'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('bulletins/', BulletinBoardListView.as_view(), name='bulletin-list'),
    path('bulletin/<int:pk>', BulletinBoardDetailView.as_view(), name='bulletin-detail'),
]
