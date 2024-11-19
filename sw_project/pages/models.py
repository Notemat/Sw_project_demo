from django.db import models

from pages.mixins import ImageTagMixin, ImageSaveMixin


class Category(ImageTagMixin, ImageSaveMixin, models.Model):
    """Модель категории продуктов на веб-странице."""

    name = models.CharField(max_length=249, verbose_name='Название продукта')
    image = models.ImageField(
        upload_to='groceries/images/',
        null=True, default=None,
        verbose_name='Изображение продукта'
    )
    image_webp = models.ImageField(
        upload_to='groceries/images/webp/',
        null=True, default=None,
        verbose_name='Изображение продукта'
    )
    description = models.TextField(verbose_name='Описание продукта')

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория продуктов'
        verbose_name_plural = 'Категории продуктов'

    def __str__(self):
        return self.name


class Element(ImageTagMixin, ImageSaveMixin, models.Model):
    """Модель элемента блока home."""

    name = models.CharField(max_length=249, verbose_name='Название элемента')
    image = models.ImageField(
        upload_to='elements/images/',
        null=True, default=None,
        verbose_name='Изображение элемента'
    )
    image_webp = models.ImageField(
        upload_to='elements/images/webp/',
        null=True, default=None,
        verbose_name='Изображение элемента'
    )
    description = models.TextField(verbose_name='Описание элемента')

    class Meta:
        ordering = ['name']
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'

    def __str__(self):
        return self.name


class Grocery(models.Model):
    """Модель отдельных продуктов."""

    category = models.OneToOneField(
        Category, related_name='grocery_detail',
        on_delete=models.CASCADE,
        verbose_name='Категория продукта'
    )
    name = models.CharField(max_length=249, verbose_name='Название продукта')
    certificate = models.ImageField(
        upload_to='certificates/',
        blank=True, null=True,
        verbose_name='Cертификат продукта'
    )
    description = models.TextField(verbose_name='Описание продукта')
    slug = models.SlugField(
        unique=True, max_length=150, verbose_name='Слаг продукта'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Страница продукта'
        verbose_name_plural = 'Страницы продуктов'

    def __str__(self):
        return self.name

    def certificate_tag(self):
        if self.certificate:
            from django.utils.html import mark_safe
            return mark_safe(
                (
                    "<img src='{}' width='350' height='350' "
                    "style='object-fit: cover;' />"
                ).format(self.certificate.url)
            )
        else:
            return 'Изображений не найдено'
    certificate_tag_short_description = 'Изображение'


class GroceryImage(ImageTagMixin, ImageSaveMixin, models.Model):
    """Модель изображений продуктов."""

    grocery = models.ForeignKey(
        Grocery, related_name='images', on_delete=models.CASCADE,
        verbose_name='Категория продукта'
    )
    image = models.ImageField(
        upload_to='grocery_images/',
        null=True, default=None,
        verbose_name='Изображение продукта'
    )
    image_webp = models.ImageField(
        upload_to='grocery_images/webp/',
        null=True, default=None,
        verbose_name='Изображение продукта'
    )
    description = models.TextField(
        default='No description', verbose_name='Описание изображения'
    )
    is_active = models.BooleanField(
        default=True, verbose_name='Отображать на странице'
    )

    class Meta:
        ordering = ['grocery']
        verbose_name = 'Изображение к продукту'
        verbose_name_plural = 'Изображения к продукту'

    def __str__(self):
        return f'Изображение к продукту - {self.grocery}'
