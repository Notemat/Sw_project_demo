import base64

import pytest
from django.core.files.base import ContentFile

from tests.constants import (
    CATEGORY_NAME, TEST_DESCRIPTION, TEST_IMAGE,
    ELEMENT_NAME, GROCERY_NAME, TEST_SLUG
)
from pages.models import Category, Grocery, GroceryImage, Element


# Функция для декодирования изображения из base64
def decode_image(base64_string):
    format, imgstr = base64_string.split(';base64,')
    ext = format.split('/')[-1]
    return ContentFile(base64.b64decode(imgstr), name=f'test_image.{ext}')


@pytest.fixture
def category_fixture(db):
    """Фикстура данных категории продуктов."""
    categories = []
    for i in range(1, 4):  # создаем три объекта
        category = Category.objects.create(
            name=f'{CATEGORY_NAME}_{i:02}',
            image=TEST_IMAGE,
            description=f'{TEST_DESCRIPTION}_{i:02}'
        )
        categories.append(category)
    return categories


@pytest.fixture
def element_fixture(db):
    """Фикстура элементов секции home"""
    elements = []
    for i in range(1, 4):
        element = Element.objects.create(
            name=f'{ELEMENT_NAME}_{i:02}',
            image=TEST_IMAGE,
            description=f'{TEST_DESCRIPTION}_{i:02}'
        )
        elements.append(element)
    return elements


@pytest.fixture
def grocery_fixture(db, category_fixture):
    """Фикстура для создания продуктов с привязкой к категориям."""
    groceries = []
    for i, category in enumerate(category_fixture):  # каждому продукту назначаем категорию
        grocery = Grocery.objects.create(
            name=f'{GROCERY_NAME}_{i+1:02}',
            category=category,  # Привязываем к категории
            description=f'{TEST_DESCRIPTION}_{i+1:02}',
            slug=f'{TEST_SLUG}-{i+1}',
            certificate=TEST_IMAGE,
        )
        groceries.append(grocery)
    return groceries


@pytest.fixture
def grocery_image_fixture(db, grocery_fixture):
    """Фикстура для создания изображений продуктов."""
    images = []
    for i, grocery in enumerate(grocery_fixture):
        image = GroceryImage.objects.create(
            grocery=grocery,
            description=f'{TEST_DESCRIPTION}_{i+1:02}',
            image=TEST_IMAGE,
        )
        images.append(image)
    return images
