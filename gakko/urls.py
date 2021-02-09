from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from django.views.generic import TemplateView
from emailer import views
from django.contrib.auth import views as auth_views
from user.views import logout_view, login_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls',
                                   'jet-dashboard')),  # Django JET dashboard URLS

    path('edu/', include('education.urls')),

    path('', include('django.contrib.auth.urls')),
    path('', include('user.urls')),



    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('send-form-email/', views.SendFormEmail.as_view(), name='send_email'),
    path('change-password/', auth_views.PasswordChangeView.as_view(
        template_name='emailer/change-password',
        success_url='/'
    ), name='change-password'),
    path('logout/', logout_view, name="logout"),
    path('login/', login_view, name="login")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
