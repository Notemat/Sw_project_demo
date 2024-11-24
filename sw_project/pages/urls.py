from django.urls import path

from pages.views import (
    GroceryDetailView,
    HomepageTemplateView,
    PrivacyPolicyTemplateView
)

app_name = 'home'

urlpatterns = [
    path(
        'grocery/<slug:slug>',
        GroceryDetailView.as_view(),
        name='grocery-detail'
    ),
    path('privacy-policy/', PrivacyPolicyTemplateView.as_view(), name='home'),
    path('', HomepageTemplateView.as_view(), name='home'),
]