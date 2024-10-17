import pytest
from django.urls import reverse


@pytest.mark.django_db
class Test_03_Templates:
    """Тесты рендеринга шаблонов."""

    def test_01_home_template(self, client):
        """Тест рендеринга шаблона главной страницы."""
        response = client.get(reverse('home:home'))
        assert response.status_code == 200
        assert 'index.html' in response.template_name

    def test_02_grocery_template(self, grocery_fixture, client):
        """Тест рендеринга шаблона страницы продукта."""
        grocery = grocery_fixture[0]
        response = client.get(reverse(
            'home:grocery-detail', kwargs={'slug': grocery.slug}
        ))
        assert response.status_code == 200
        assert 'grocery_detail.html' in response.template_name
