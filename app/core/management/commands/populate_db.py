import csv

from django.apps import apps
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Populate the DB using csv files, from data folder"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, help="File Path")
        parser.add_argument("--model_name", type=str, help="Model Name")
        parser.add_argument("--app_name", type=str, help="Django App")

    def handle(self, *args, **options):
        # TODO: check bulk_create
        file_path = options["path"]
        model = apps.get_model(options["app_name"], options["model_name"])
        with open(file_path, "r") as csv_file:
            reader = csv.reader(csv_file, delimiter=";", lineterminator="\n")
            header = next(reader)
            for row in reader:
                object_dict = {key: value for key, value in zip(header, row)}
                model.objects.get_or_create(**object_dict)
