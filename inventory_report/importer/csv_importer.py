import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @classmethod
    def import_data(cls, path):
        with open(path, "r") as file:
            try:
                products = csv.DictReader(file, delimiter=",")
                return [product for product in products]
            except Exception:
                raise ValueError("Arquivo inválido")
