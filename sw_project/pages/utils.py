from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


def save_image_in_multiple_formats(uploaded_file):
    """
    Утилита для сохранения изображения в двух форматах (исходном и .webp).
    """
    # Открываем загруженный файл как изображение
    original_image = Image.open(uploaded_file)

    # Сохраняем изображение в оригинальном формате
    original_image_io = BytesIO()
    original_image.save(original_image_io, format=original_image.format)
    original_image_content = ContentFile(
        original_image_io.getvalue(), name=uploaded_file.name
    )

    # Конвертируем и сохраняем изображение в формате WebP
    webp_image_io = BytesIO()
    original_image.save(webp_image_io, format='WEBP')
    webp_image_content = ContentFile(
        webp_image_io.getvalue(),
        name=f'{uploaded_file.name.split(".")[0]}.webp'
    )

    # Возвращаем оригинальный и WebP-форматы для последующего сохранения
    return original_image_content, webp_image_content
