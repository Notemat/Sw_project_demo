from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.utils.safestring import mark_safe

from pages.mixins import ImagePreviewMixin
from pages.models import (
    Element,
    Grocery,
    GroceryImage,
    GroceryValue,
    MeasurementUnit,
)


admin.site.unregister(User)
admin.site.unregister(Group)


class PriceAdminForm(forms.ModelForm):
    class Meta:
        model = GroceryImage
        fields = ('price', )
        widgets = {
            'price': forms.TextInput(attrs={'placeholder': 'Цена в ₽'})
        }


class GroceryValueInline(admin.TabularInline):
    """Инлайн объема тары продукта."""
    model = GroceryValue
    extra = 1
    autocomplete_fields = ['measurement_unit']


@admin.register(Element)
class ElementAdmin(ImagePreviewMixin, admin.ModelAdmin):
    """Модель продукта в админке."""

    list_display = (
        'name', 'description', 'priority', 'is_active', 'image_preview'
    )
    list_editable = ('description', 'priority', 'is_active')
    search_fields = ('name', )
    readonly_fields = ('image_tag',)
    fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': (
                ('name', 'char_limit', 'is_active'),
                ('description'), ('action_link', 'priority'),
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
    """Модель категорий в админке."""

    list_display = ('name', 'priority', 'slug', 'image_count', 'image_preview')
    search_fields = ('name', )
    readonly_fields = ('certificate_tag', 'image_tag')
    list_editable = ('priority',)
    fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': (
                ('name', 'slug', 'priority',),
                ('main_description'), ('description'),
            ),
        }),
        ('HTML-файлы', {
            'classes': ('wide', 'collapse'),
            'fields': (
                ('image', 'image_tag'),
                ('certificate', 'certificate_tag'),
            )
        }),
    )

    @admin.display(description='Количество продуктов в карусели')
    def image_count(self, obj):
        return obj.images.count()

    @admin.display(description='Предпросмотр изображений')
    def image_preview(self, obj):
        """Отображает изображение в админке как HTML-картинку."""
        if obj.image:
            return mark_safe(
                f'<img src="{obj.image.url}" width="50" />'
            )
        return "Нет изображения"


@admin.register(GroceryImage)
class GroceryImagelAdmin(ImagePreviewMixin, admin.ModelAdmin):
    """Модель отдельного продукта в админке."""

    list_display = (
        'description', 'image_preview', 'is_active', 'price', 'grocery'
    )
    inlines = [GroceryValueInline]
    form = PriceAdminForm
    search_fields = ['description', ]
    list_filter = ('grocery', )
    list_editable = ('is_active', 'price')
    readonly_fields = ('image_tag',)
    autocomplete_fields = ('grocery', )
    fieldsets = (
        (None, {
            'classes': ('wide'),
            'fields': (
                ('grocery', 'is_active'),
                ('description', 'price'),
            ),
        }),
        ('HTML-файлы', {
            'classes': ('wide', 'collapse'),
            'fields': (('image', 'image_tag'),)
        }),
    )
