import sys
from inventory_report.inventory.inventory_refactor import InventoryRefactor
from inventory_report.importer.importer_factory import ImporterFactory


def main():
    try:
        path = sys.argv[1]
        report_type = sys.argv[2]
    except IndexError:
        return print("Verifique os argumentos", file=sys.stderr)

    importer = ImporterFactory.generate(path)
    inventory = InventoryRefactor(importer)
    report = inventory.import_data(path, report_type)
    print(report, end="")


if __name__ == "__main__":
    main()
