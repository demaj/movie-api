import csv

from django.apps import apps
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Populate the DB using csv files, from data folder"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, help="File path")
        parser.add_argument("--model_name", type=str, help="Model name")
        parser.add_argument("--app_name", type=str, help="Django app name")

    def handle(self, *args, **options):
        # TODO: check bulk_create
        file_path = options["path"]
        app_name = options["app_name"]
        model_name = options["model_name"]

        model = apps.get_model(app_name, model_name)

        with open(file_path, "r") as csv_file:
            reader = csv.DictReader(csv_file, delimiter=";", lineterminator="\n")
            rows = [model(**row) for row in reader]
            model.objects.bulk_create(rows, ignore_conflicts=True)
