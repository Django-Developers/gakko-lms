from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS

    path('',include('django.contrib.auth.urls')),
    path('',include('user.urls')),
    path('edu/',include('education.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


