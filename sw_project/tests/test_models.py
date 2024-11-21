import pytest
from tests.constants import (
    CATEGORY_NAME,
    ELEMENT_NAME,
    GROCERY_NAME,
    OBJECT_COUNT,
    TEST_SLUG,
)


@pytest.mark.django_db
class Test_01_Models:
    """Проверяем создание объектов моделей."""

    def test_01_category_creation(self, category_fixture):
        """Проверяем создание категорий."""
        assert len(category_fixture) == OBJECT_COUNT

        for category in category_fixture:
            assert category.name is not None
            assert category.description is not None
            assert category.image is not None
            assert category.name.startswith(CATEGORY_NAME)

    def test_02_element_creation(self, element_fixture):
        """Проверяем создание категорий."""
        assert len(element_fixture) == OBJECT_COUNT

        for element in element_fixture:
            assert element.name is not None
            assert element.description is not None
            assert element.image is not None
            assert element.name.startswith(ELEMENT_NAME)

    def test_03_grocery_creation(self, grocery_fixture):
        """Проверяем создание категорий."""
        assert len(grocery_fixture) == OBJECT_COUNT

        for grocery in grocery_fixture:
            assert grocery.name is not None
            assert grocery.description is not None
            assert grocery.certificate is not None
            assert grocery.slug is not None
            assert grocery.name.startswith(GROCERY_NAME)
            assert grocery.slug.startswith(TEST_SLUG)

    def test_04_grocery_image_creation(self, grocery_image_fixture):
        """Проверяем создание категорий."""
        assert len(grocery_image_fixture) == OBJECT_COUNT

        for grocery_image in grocery_image_fixture:
            assert grocery_image.grocery is not None
            assert grocery_image.description is not None
            assert grocery_image.image is not None
            assert grocery_image.grocery.name.startswith(GROCERY_NAME)
