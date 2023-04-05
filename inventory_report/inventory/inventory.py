from inventory_report.reports.report_factory import ReportFactory
from inventory_report.importer.importer_factory import ImporterFactory


class Inventory:
    @classmethod
    def import_data(cls, path, report_type):
        importer = ImporterFactory.generate(path)
        inventory_items = importer.import_data(path)
        report = ReportFactory.generate(report_type, inventory_items)
        return report
