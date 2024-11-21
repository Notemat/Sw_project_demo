from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, URLPattern, URLResolver
from typing import List, Union

from pages.views import custom_permission_denied, page_not_found, server_error


urlpatterns: List[Union[URLPattern, URLResolver]] = [
    path(settings.ADMIN_URL, admin.site.urls),
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

handler403 = custom_permission_denied

handler404 = page_not_found

handler500 = server_error
