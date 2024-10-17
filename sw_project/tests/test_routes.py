import pytest
from django.urls import reverse


@pytest.mark.django_db
class Test_02_Routes:
    """Тесты доступности маршрутов."""

    def test_01_home_page(self, client):
        """Тест доступности главной страницы."""
        response = client.get(reverse('home:home'))

        assert response.status_code == 200

    def test_02_grocery_detail_page(self, grocery_fixture, client):
        """Тесты доступности страницы продукта."""
        grocery = grocery_fixture[0]
        response = client.get(reverse(
            'home:grocery-detail', kwargs={'slug': grocery.slug}
        ))
        assert response.status_code == 200
        assert grocery.name in response.content.decode()
        assert grocery.description in response.content.decode()