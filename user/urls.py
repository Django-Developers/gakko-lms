from django.urls import path

from django.views.generic import TemplateView
from emailer.views import SendFormEmail
from django.contrib.auth import views as auth_views
from user import views



urlpatterns = [

    path('profile/', views.profile, name='profile'),
    path('register/', views.register, name='register'),


    path('send-form-email/', SendFormEmail.as_view(), name='send-email'),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='emailer/change-password',
        success_url='/'
    ), name='change-password'),


    path('logout/', views.logout_view, name="logout"),
    path('login/', views.login_view, name="login"),

    path('', views.index, name='index'),

    # path('update_profile/<str:pk/>',views.updateProfile,name="update")
    # path('', TemplateView.as_view(template_name="home.html"), name='home'),


]
