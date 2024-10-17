from django.utils.safestring import mark_safe


class ImagePreviewMixin:
    """Миксин для отображения изображений в админке."""

    def image_preview(self, obj, field_name='image'):
        """Отображает изображение в админке как HTML-картинку."""
        image = getattr(obj, field_name, None)
        if image:
            return mark_safe(f'<img src="{image.url}" width="50" />')
        return "Нет изображения"


class ImageTagMixin:
    """Миксин для отображения превью изображений в админке для моделей."""

    def image_tag(self):
        if self.image:
            from django.utils.html import mark_safe
            return mark_safe(
                (
                    "<img src='{}' width='350' height='350' "
                    "style='object-fit: cover;' />"
                ).format(self.image.url)
            )
        else:
            return 'Изображений не найдено'
    image_tag_short_description = 'Изображение'