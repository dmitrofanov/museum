from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from museum.views import api_root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api_root, name='api-root'),
    path('api/', include('museum.urls')),
]

# Для обслуживания медиа-файлов в режиме разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)