from django.conf.urls.static import static
from django.urls import path, include

from . import settings

urlpatterns = [
    path('', include('main.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
