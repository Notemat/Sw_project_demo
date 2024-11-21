from django.conf import settings
from django.shortcuts import render


class RestrictAdminAccessMiddleware:
    """Мидлвэйр для ограничения доступа к админке по ip-адресу"""
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Получение разрешенных IP из settings.py
        allowed_ips = getattr(settings, 'ALLOWED_ADMIN_IPS', [])

        # Проверяем, начинается ли путь с и совпадает ли IP
        client_ip = request.META.get('REMOTE_ADDR')
        admin_url = f'/{settings.ADMIN_URL.strip("/")}/'
        if request.path.startswith(admin_url) and client_ip not in allowed_ips:
            return render(request, 'errors/403.html', status=403)

        # Передаём запрос дальше
        return self.get_response(request)
