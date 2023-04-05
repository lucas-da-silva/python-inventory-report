from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport

BLUE = "\033[36m"
GREEN = "\033[32m"
RED = "\033[31m"
RESET = "\033[0m"


def test_decorar_relatorio():
    company_with_more_products = "Coca-Cola Company"
    oldest_date = "2020-01-01"
    nearest_expiration_date = "2024-12-31"
    products_list = [
        {
            "id": 1,
            "nome_do_produto": "Coca-Cola",
            "nome_da_empresa": company_with_more_products,
            "data_de_fabricacao": oldest_date,
            "data_de_validade": nearest_expiration_date,
            "numero_de_serie": "123456789",
            "instrucoes_de_armazenamento": "Manter em local seco",
        }
    ]
    report = ColoredReport(SimpleReport).generate(products_list)

    assert f"{GREEN}Data de fabricação mais antiga:{RESET}" in report
    assert f"{GREEN}Data de validade mais próxima:{RESET}" in report
    assert f"{GREEN}Empresa com mais produtos:{RESET}" in report
    assert f"{BLUE}{oldest_date}{RESET}" in report
    assert f"{BLUE}{nearest_expiration_date}{RESET}" in report
    assert f"{RED}{company_with_more_products}{RESET}" in report
