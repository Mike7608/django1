from profile import Profile

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


@register.filter()
def show_button(creator, user):
    """
    Процедуоа сравнивает создателя записи блога с активным пользователем
    если они идентичны, возвращает True
    P.S. Можно использовать для отключения кнопок на форме
    """
    if str(creator).lower() == str(user.user.email).lower():
        return True
    else:
        return False
