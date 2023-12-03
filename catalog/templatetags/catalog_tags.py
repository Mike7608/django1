from django import template
from django.urls import reverse

register = template.Library()


@register.simple_tag
def catalog_url(url_name):
    return reverse(url_name)
