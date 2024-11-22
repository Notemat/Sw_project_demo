from django.contrib import admin
from django.db import models
from django.utils.html import mark_safe

from pages.mixins import ImageSaveMixin, ImageTagMixin


class Element(ImageTagMixin, ImageSaveMixin, models.Model):
    """Модель элемента блока home."""

    name: models.CharField = models.CharField(
        max_length=249, verbose_name='Название элемента'
    )
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
    description: models.TextField = models.TextField(
        verbose_name='Описание элемента'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Элемент'
        verbose_name_plural = 'Элементы'

    def __str__(self):
        return self.name


class MeasurementUnit(models.Model):
    """Модель единицы измерения."""

    name: models.CharField = models.CharField(
        max_length=50, verbose_name='Полное название единицы измерения'
    )
    abbreviation: models.CharField = models.CharField(
        max_length=5, verbose_name='Сокращение единицы измерения'
    )

    class Meta:
        ordering = ['abbreviation']
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'

    def __str__(self):
        return f'{self.abbreviation}'


class Grocery(ImageTagMixin, ImageSaveMixin, models.Model):
    """Модель отдельных продуктов."""

    name: models.CharField = models.CharField(
        max_length=249, verbose_name='Название продукта'
    )
    certificate = models.ImageField(
        upload_to='certificates/',
        blank=True, null=True,
        verbose_name='Cертификат продукта'
    )
    image = models.ImageField(
        upload_to='groceries/images/',
        null=True, default=None,
        verbose_name='Изображение категории продукта'
    )
    image_webp = models.ImageField(
        upload_to='groceries/images/webp/',
        null=True, default=None,
        verbose_name='Изображение категории продукта'
    )
    main_description: models.TextField = models.TextField(
        verbose_name='Описание на главной странице'
    )

    description: models.TextField = models.TextField(
        verbose_name='Описание на странице продуктов'
    )
    slug: models.SlugField = models.SlugField(
        unique=True, max_length=150, verbose_name='Слаг продукта'
    )

    class Meta:
        ordering = ['name']
        verbose_name = 'Категория продукта'
        verbose_name_plural = 'Категории продуктов'

    def __str__(self):
        return self.name

    @admin.display(description='Сертификат')
    def certificate_tag(self):
        if self.certificate:
            return mark_safe(
                (
                    "<img src='{}' width='350' height='350' "
                    "style='object-fit: cover;' />"
                ).format(self.certificate.url)
            )
        else:
            return 'Сертификатов не найдено'

    @admin.display(description='Изображение')
    def image_tag(self):
        if self.image_webp:
            return mark_safe(
                (
                    "<img src='{}' width='350' height='350' "
                    "style='object-fit: cover;' />"
                ).format(self.image.url)
            )
        else:
            return 'Изображений не найдено'


class GroceryImage(ImageTagMixin, ImageSaveMixin, models.Model):
    """Модель изображений продуктов."""

    grocery: models.ForeignKey = models.ForeignKey(
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
    description: models.TextField = models.TextField(
        default='No description', verbose_name='Описание изображения'
    )
    is_active: models.BooleanField = models.BooleanField(
        default=True, verbose_name='Отображать на странице'
    )

    class Meta:
        ordering = ['grocery']
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return f'Продукт категории - {self.grocery}'


class GroceryValue(models.Model):
    """Модель объёма тары продутка."""

    grocery_image: models.ForeignKey = models.ForeignKey(
        GroceryImage,
        related_name='volumes',
        on_delete=models.CASCADE,
        verbose_name='Продукт'
    )
    value: models.PositiveIntegerField = models.PositiveIntegerField(
        verbose_name='Объём тары продукта'
    )
    measurement_unit: models.ForeignKey = models.ForeignKey(
        MeasurementUnit,
        on_delete=models.PROTECT,
        verbose_name='Единица измерения'
    )

    class Meta:
        ordering = ['grocery_image']
        verbose_name = 'Объём тары продукта'
        verbose_name_plural = 'Объём тары продуктов'

    def __str__(self):
        return f'{self.value} {self.measurement_unit}'
