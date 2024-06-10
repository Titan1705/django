from django.core.management import BaseCommand
from catalog.models import Category, Product
import json


class Command(BaseCommand):

    @staticmethod
    def json_read_categories():
    # Получаем данные из фикстуры с категориями
        with open('category.json', encoding='utf-8') as file:
            return json.load(file)

    @staticmethod
    def json_read_products():
    # Получаем данные из фикстуры с продуктами
        with open('product.json', encoding='utf-8') as file:
            return json.load(file)

    def handle(self, *args, **options):

        Category.objects.all().delete() # Удаляем все категории
        Product.objects.all().delete() # Удаляем все продукты

        # Создаем списки для хранения объектов
        category_list = []
        # Обходим все значения категорий из фикстуры для получения информации об одном объекте
        for category in Command.json_read_categories():
            category_list.append(
                {
                    "id": category['pk'],
                    "name": category['fields']['name'],
                    "description": category['fields']['description']
                }
                )

        category_for_create = []
        for category_item in category_list:
            category_for_create.append(
                Category.objects.create(**category_item)
            )

        product_list = []
        # Обходим все значения продуктов из фикстуры для получения информации об одном объекте
        for product in Command.json_read_products():
            product_list.append(
                {
                    "id": product['pk'],
                    "name": product['fields']['name'],
                    "description": product['fields']['description'],
                    "photo": product['fields']['photo'],
                    "category": Category.objects.get(pk=product['fields']['category']),
                    "price": product['fields']['price'],
                    "created_at": product['fields']['created_at'],
                    "updated_at": product['fields']['updated_at']

                }
                )

        product_for_create = []
        for product_item in product_list:
            product_for_create.append(
                Product.objects.create(**product_item)
            )

        # Создаем объекты в базе с помощью метода bulk_create()
        Category.objects.bulk_create(category_for_create)
        Product.objects.bulk_create(product_for_create)