from django import template
from django.conf import settings

register = template.Library()


@register.filter()
def text_to_html(text, view_str=0):
    list_znak = ['& &amp', '< &lt', '> &gt', '" &quot', "' &#39"]
    # '\t &emsp'
    for z in list_znak:
        list_z = z.split()
        text = text.replace(list_z[0], list_z[1])

    text = "<br>".join(text.split("\r\n"))
    text = "<br>".join(text.split("\n"))

    count_str = text.count("<br>")

    if count_str >= view_str > 0:
        str_list = text.split("<br>")
        text = ""

        for index in range(view_str):
            text += str_list[index]
            text += "<br>"

    return text
