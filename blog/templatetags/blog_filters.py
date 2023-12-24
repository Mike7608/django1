from django import template

from blog.models import Version

register = template.Library()


@register.filter()
def actual_version(pk):
    """
    Процедура возвращает актуальную версию
    """
    version = Version.objects.all()
    ver = ''
    for v in version:
        if v.blog.pk == pk:
            if v.sign:
                ver = f"Актуальная версия: {v.version}"

    return ver
