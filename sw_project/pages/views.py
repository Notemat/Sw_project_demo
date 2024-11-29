from django.shortcuts import render
from django.views.generic import DetailView, TemplateView

from pages.constants import META_GROCERIES, META_TAGS
from pages.models import Element, Grocery


class HomepageTemplateView(TemplateView):
    '''Класс главной страницы.'''

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['elements'] = Element.objects.all()
        context['groceries'] = Grocery.objects.all()
        return context


class GroceryDetailView(DetailView):
    '''Клас отдельного продукта в категории.'''
    model = Grocery
    template_name = 'grocery_detail.html'
    context_object_name = 'grocery'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()

        meta_description = META_GROCERIES
        for key, description in META_TAGS.items():
            if key in self.request.path.lower():
                meta_description = description
                break
        context['meta_description'] = meta_description
        return context


class PrivacyPolicyTemplateView(TemplateView):
    '''Класс страницы политики конфиденциальности.'''

    template_name = 'privacy_policy.html'


def page_not_found(request, exception):
    '''Кастомная страница ошибки 404'''
    return render(request, 'errors/404.html', status=404)


def server_error(request):
    '''Кастомная страница ошибки 500.'''
    return render(request, 'errors/500.html', status=500)


def custom_permission_denied(request, exception=None):
    return render(request, 'errors/403.html', status=403)
