from django.http import HttpResponseForbidden
from django.conf import settings


class RestrictAdminAccessMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Получение разрешенных IP из settings.py
        allowed_ips = getattr(settings, 'ALLOWED_ADMIN_IPS', [])

        # Проверяем, начинается ли путь с /admin/ и совпадает ли IP
        client_ip = request.META.get('REMOTE_ADDR')
        if request.path.startswith('/admin/') and client_ip not in allowed_ips:
            return HttpResponseForbidden("Access denied")

        # Передаём запрос дальше
        return self.get_response(request)