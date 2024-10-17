from django.urls import path

from pages.views import GroceryDetailView, HomepageTemplateView

app_name = 'home'

urlpatterns = [
    path(
        'grocery/<slug:slug>',
        GroceryDetailView.as_view(),
        name='grocery-detail'
    ),
    path('', HomepageTemplateView.as_view(), name='home'),
]