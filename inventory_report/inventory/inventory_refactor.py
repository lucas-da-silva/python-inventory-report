from collections.abc import Iterable
from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.report_factory import ReportFactory


class InventoryRefactor(Iterable):
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path, report_type):
        inventory_items = self.importer.import_data(path)
        report = ReportFactory.generate(report_type, inventory_items)
        for item in inventory_items:
            self.data.append(item)
        return report

    def __iter__(self):
        return InventoryIterator(self.data)
