from django.urls import path
from user import views

urlpatterns =[
    path('',views.index, name='index'),
    path('profile/',views.profile, name='profile'),
    path('register/',views.register, name='register')

    #path('update_profile/<str:pk/>',views.updateProfile,name="update")
    

]