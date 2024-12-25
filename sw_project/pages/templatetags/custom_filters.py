from django import template

register = template.Library()


@register.filter
def truncate_words(value, char_count):
    """
    Обрезает текст до целого слова и добавляет многоточие, если текст длинный.
    """
    if not isinstance(value, str):
        return value

    if len(value) <= char_count:
        return value

    truncated = value[:char_count].rsplit(" ", 1)[0]
    return truncated + "..."
