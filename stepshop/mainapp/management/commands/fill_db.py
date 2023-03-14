import json
import os

from django.contrib.auth.models import User
from django.core import management
from django.core.management import BaseCommand

from authapp.models import ShopUser
from mainapp.models import ProductCategory, Product

JSON_PATH = os.path.join('mainapp', 'fixtures')


def load_from_json(file_name):
    with open(os.path.join(JSON_PATH, file_name), mode='r', encoding='utf-8') as file:
        return json.load(file)


class Command(BaseCommand):
    def handle(self, *args, **options):
        management.call_command('flush', verbosity=0, interactive=False)

        categories = load_from_json('categories.json')
        # ProductCategory.objects.all().delete()

        for category in categories:
            new_category = category.get('fields')
            new_category['id'] = category.get('pk')

            category_db = ProductCategory(**new_category)
            category_db.save()

        products = load_from_json('products.json')
        # Product.objects.all().delete()

        for product in products:
            new_product = product.get('fields')
            category_id = new_product['category']
            new_product['category'] = ProductCategory.objects.get(pk=category_id)

            product_db = Product(**new_product)
            product_db.save()

        # User.objects.create_superuser('admin', 'admin@stepshop.local', '123')
        ShopUser.objects.create_superuser('admin', 'admin@stepshop.local', '123', age=18)
