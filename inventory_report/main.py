import sys
from inventory_report.importer.importer_factory import ImporterFactory
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport

REPORTER_MAPPING = {
    "simples": SimpleReport,
    "completo": CompleteReport,
}


def main():
    try:
        path = sys.argv[1]
        report_type = sys.argv[2]
    except IndexError:
        return print("Verifique os argumentos", file=sys.stderr)

    importer = ImporterFactory.generate(path)
    inventory = InventoryRefactor(importer)
    inventory.import_data(path, report_type)
    colored_report = ColoredReport(REPORTER_MAPPING[report_type])
    report = colored_report.generate(inventory.data)
    print(report, end="")


if __name__ == "__main__":
    main()
