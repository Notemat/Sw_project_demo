from django.contrib import admin
from django.contrib.auth.models import User, Group
from django.utils.safestring import mark_safe

from pages.models import (
    Element, Category, Grocery,
    GroceryImage, GroceryValue, MeasurementUnit
)
from pages.mixins import ImagePreviewMixin


admin.site.unregister(User)
admin.site.unregister(Group)


class GroceryImageInline(ImagePreviewMixin, admin.TabularInline):
    """Инлайн продукта."""
    model = GroceryImage
    extra = 1


class GroceryValueInline(admin.TabularInline):
    """Инлайн объема тары продукта."""
    model = GroceryValue
    extra = 1
    autocomplete_fields = ['measurement_unit']


@admin.register(Category)
class CategoryAdmin(ImagePreviewMixin, admin.ModelAdmin):
    """Модель категории продукта в админке."""

    list_display = ('name', 'image_preview')
    search_fields = ('name', )
    readonly_fields = ('image_tag',)
    fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': (
                ('name'),
                ('description'),
            ),
        }),
        ('HTML-файлы', {
            'classes': ('wide', 'collapse'),
            'fields': (('image', 'image_tag'),)
        }),
    )


@admin.register(Element)
class ElementAdmin(ImagePreviewMixin, admin.ModelAdmin):
    """Модель продукта в админке."""

    list_display = ('name', 'description', 'image_preview')
    list_editable = ('description', )
    search_fields = ('name', )
    readonly_fields = ('image_tag',)
    fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': (
                ('name'),
                ('description'),
            ),
        }),
        ('HTML-файлы', {
            'classes': ('wide', 'collapse'),
            'fields': (('image', 'image_tag'),)
        }),
    )


@admin.register(MeasurementUnit)
class MeasurementUnitAdmin(admin.ModelAdmin):
    """Модель единицы измерения в админке."""

    list_display = ('name', 'abbreviation')
    search_fields = ('name', )


@admin.register(Grocery)
class GroceryDetailAdmin(admin.ModelAdmin):
    """Модель продукта в админке."""

    list_display = ('name', 'slug', 'image_count', 'image_preview')
    search_fields = ('name', )
    readonly_fields = ('certificate_tag',)
    fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': (
                ('name', 'slug', 'category'),
                ('description'),
            ),
        }),
        ('HTML-файлы', {
            'classes': ('wide', 'collapse'),
            'fields': (('certificate', 'certificate_tag'),)
        }),
    )
    inlines = [GroceryImageInline]

    @admin.display(description='Количество изображений')
    def image_count(self, obj):
        return obj.images.count()

    @admin.display(description='Предпросмотр изображений')
    def image_preview(self, obj):
        """Отображает изображение в админке как HTML-картинку."""
        first_image = obj.images.first()
        if first_image:
            return mark_safe(
                f'<img src="{first_image.image.url}" width="50" />'
            )
        if obj.certificate:
            return mark_safe(
                f'<img src="{obj.certificate.url}" width="50" />'
            )
        return "Нет изображения"


@admin.register(GroceryImage)
class GroceryImagelAdmin(ImagePreviewMixin, admin.ModelAdmin):
    """Модель изображения продукта в админке."""

    list_display = ('description', 'image_preview', 'is_active', 'grocery')
    inlines = [GroceryValueInline]
    search_fields = ['description', ]
    list_filter = ('grocery', )
    list_editable = ('is_active',)
    readonly_fields = ('image_tag',)
    autocomplete_fields = ('grocery', )
    fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': (
                ('grocery', 'is_active'),
                ('description'),
            ),
        }),
        ('HTML-файлы', {
            'classes': ('wide', 'collapse'),
            'fields': (('image', 'image_tag'),)
        }),
    )
