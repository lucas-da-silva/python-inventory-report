import os
from inventory_report.reports.report_factory import ReportFactory
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.xml_importer import XmlImporter

importer_mapping = {
    ".json": JsonImporter,
    ".csv": CsvImporter,
    ".xml": XmlImporter,
}


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        file_extension = os.path.splitext(path)[1]
        importer = importer_mapping[file_extension]
        inventory_items = importer.import_data(path)
        report = ReportFactory.generate(report_type, inventory_items)
        return report
