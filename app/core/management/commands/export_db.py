import csv

from django.apps import apps
from django.core.management import BaseCommand


class Command(BaseCommand):
    help = "Export data from a specific model in the database to a CSV file"

    def add_arguments(self, parser):
        parser.add_argument("--path", type=str, help="File path")
        parser.add_argument("--model_name", type=str, help="Model name")
        parser.add_argument("--app_name", type=str, help="Django app name")

    def handle(self, *args, **options):
        file_path = options["path"]
        app_name = options["app_name"]
        model_name = options["model_name"]

        model = apps.get_model(app_name, model_name)

        with open(file_path, "w", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=";", lineterminator="\n")

            # Write the header row
            field_names = [field.name for field in model._meta.fields]
            writer.writerow(field_names)

            # Write the data row by row
            for obj in model.objects.all():
                row_data = [getattr(obj, field_name) for field_name in field_names]
                writer.writerow(row_data)
