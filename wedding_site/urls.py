from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from core import views  # se la tua app si chiama "core"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_photo, name='upload'),  # opzionale se hai la view
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
