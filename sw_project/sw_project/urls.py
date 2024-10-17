from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from pages.views import server_error, page_not_found


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('pages.urls', namespace='home'))
]

if settings.DEBUG:
    # Раздача медиа-файлов
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

handler404 = page_not_found

handler500 = server_error
