import os

from django.utils.safestring import mark_safe

from pages.utils import save_image_in_multiple_formats


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


class ImageSaveMixin:
    """Миксин для сохраниения изображений в нужном формате."""

    def save(self, *args, **kwargs):
        if self.image:
            # Проверяем формат загружаемого файла
            file_name, file_extension = os.path.splitext(self.image.name)
            file_extension = file_extension.lower()

            if file_extension == ".webp":
                # Если файл уже в формате WEBP, сохраняем его в image_webp
                self.image_webp.save(self.image.name, self.image, save=False)
                self.image.save(self.image.name, self.image, save=False)
            else:
                image_file, webp_file = save_image_in_multiple_formats(
                    self.image
                )

                self.image.save(image_file.name, image_file, save=False)
                self.image_webp.save(webp_file.name, webp_file, save=False)

        super().save(*args, **kwargs)