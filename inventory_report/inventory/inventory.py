import os
from enum import Enum
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter

importer_mapping = {
    ".json": JsonImporter,
    ".csv": CsvImporter,
    ".xml": XmlImporter,
}


class ReportType(Enum):
    SIMPLE = "simples"
    COMPLETE = "completo"


class ReportFactory:
    @staticmethod
    def generate(report_type, inventory_items):
        if report_type == ReportType.SIMPLE.value:
            return SimpleReport.generate(inventory_items)
        elif report_type == ReportType.COMPLETE.value:
            return CompleteReport.generate(inventory_items)


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        file_extension = os.path.splitext(path)[1]
        importer = importer_mapping[file_extension]
        inventory_items = importer.import_data(path)
        report = ReportFactory.generate(report_type, inventory_items)
        return report
