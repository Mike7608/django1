import django.forms.fields
from django import forms
from blog.models import Blog, Version

# запрещенные слова
PROHIBITED_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():

            if type(field) is not django.forms.fields.BooleanField:
                field.widget.attrs['class'] = 'form-control'


class BlogForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Blog
        exclude = ('slug', 'total_view')

    def clean_heading(self):
        """
        Проверяем поле Заголовка на запрещенные слова
        """
        cleaned_data = self.cleaned_data.get('heading')

        if cleaned_data in PROHIBITED_WORDS:
            raise forms.ValidationError('Ошибка! Заголовок содержит недопустимые слова.')

        return cleaned_data

    def clean_text(self):
        """
        Проверяем поле Содержание на запрещенные слова
        """
        cleaned_data = self.cleaned_data.get('text')

        if cleaned_data in PROHIBITED_WORDS:
            raise forms.ValidationError('Ошибка! Текст публикации содержит недопустимые слова.')

        return cleaned_data


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'
