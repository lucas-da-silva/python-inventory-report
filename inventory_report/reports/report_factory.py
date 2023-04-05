from enum import Enum
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


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
