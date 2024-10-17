from typing import Any
from django.views.generic import DetailView, TemplateView
from django.shortcuts import render

from pages.models import Element, Category, Grocery


class HomepageTemplateView(TemplateView):
    """Класс главной страницы."""

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.prefetch_related(
            'grocery_detail'
        ).order_by('-id')
        context['elements'] = Element.objects.all()
        context['grocery'] = Grocery.objects.all()
        return context


def product_list(request):
    products = Category.objects.all()
    return render(request, 'index.html', {'products': products})


def element_list(request):
    elements = Element.objects.all()
    return render(request, 'index.html', {'elements': elements})


class GroceryDetailView(DetailView):
    """Клас отдельного продукта в категории."""
    model = Grocery
    template_name = 'grocery_detail.html'
    context_object_name = 'grocery'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['images'] = self.object.images.all()
        return context


def page_not_found(request, exception):
    """Кастомная страница ошибки 404"""
    return render(request, 'errors/404.html', status=404)


def server_error(request):
    """Кастомная страница ошибки 500."""
    return render(request, 'errors/500.html', status=500)
