from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('vehicles.urls')),
    path('parts/', include('parts.urls')),
    path('auth/', include('allauth.urls')),
    path('login/', include('login.urls')),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
