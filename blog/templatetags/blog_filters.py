from django import template

from blog.models import Version

register = template.Library()


@register.filter()
def actual_version(pk):
    """
    Процедура возвращает актуальную версию
    """
    version = Version.objects.all()
    ver = 'отсутствует'
    for v in version:
        if v.blog.pk == pk:
            if v.sign:
                ver = v.version

    return f"Актуальная версия: {ver}"
