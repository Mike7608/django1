from django.core.management import BaseCommand
import json
from catalog.models import Category, Product


def json_to_dict():
    """
    Функция возвращает данные из JSON в списки Category, Product
    """
    category = []
    products = []

    with open('data.json', 'r') as f:
        try:
            data = json.load(f)

            for item in data:
                if item['model'] == "catalog.category":
                    category.append(item)
                if item['model'] == "catalog.product":
                    products.append(item)

        except ValueError:
            print("Ошибка файла или кодировки!")

    return category, products


class Command(BaseCommand):
    """
    Команда Fill заполняет данными БД из файла data.json
    """
    def handle(self, *args, **options):

        category, products = json_to_dict()

        Category.objects.all().delete()

        for item_cat in category:

            id_cat = item_cat['pk']

            cat = Category(id=id_cat,
                           name=item_cat['fields']['name'],
                           description=item_cat['fields']['description'])

            cat.save()

            for item_prod in products:

                if item_prod['fields']['category'] == id_cat:

                    product = Product(name=item_prod['fields']['name'],
                                      description=item_prod['fields']['description'],
                                      pict=item_prod['fields']['pict'],
                                      category=cat,
                                      price=item_prod['fields']['price'],
                                      date_create=item_prod['fields']['date_create'],
                                      date_edit=item_prod['fields']['date_edit'])
                    product.save()
