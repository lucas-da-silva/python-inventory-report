import os
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter

IMPORTER_MAPPING = {
    ".json": JsonImporter,
    ".csv": CsvImporter,
    ".xml": XmlImporter,
}


class ImporterFactory:
    @classmethod
    def generate(cls, file_path: str):
        file_extension = os.path.splitext(file_path)[1]
        importer = IMPORTER_MAPPING[file_extension]
        return importer
