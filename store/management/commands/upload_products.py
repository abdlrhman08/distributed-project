import argparse
import csv
import os
import re

from django.core.management.base import BaseCommand
from openai import OpenAI

from store.models import Category, Product


class Command(BaseCommand):
    help = "Upload initial data to database"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    
    def add_arguments(self, parser):
        parser.add_argument("filepath", nargs=1, action="store", type=argparse.FileType('r'))

    def handle(self, **options):
        filepath = options["filepath"][0]
        csv_data = csv.DictReader(filepath)

        category_name = os.path.basename(filepath.name).split("Data")[0]
        Category.objects.get_or_create(name=category_name)

        object_set = set()
        products = []
        for row in csv_data:
            if row["Price"] and row["Name"] not in object_set:
                object_set.add(row["Name"])
                price = float(re.findall("\d+\.\d+", row["Price"])[0])
                products.append(Product(
                    name=row["Name"],
                    price=price
                ))
