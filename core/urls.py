from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
    path('mentoring/', include("mentoring.urls")),
    path('podcast/', include('podcast.urls'), name="podcast"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
