from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @classmethod
    def generate(cls, products):
        products_by_company = {}
        products_by_company_str = ""
        
        for product in products:
            if product["nome_da_empresa"] in products_by_company:
                products_by_company[product["nome_da_empresa"]] += 1
            else:
                products_by_company[product["nome_da_empresa"]] = 1

        for company, quantity in products_by_company.items():
            products_by_company_str += f"- {company}: {quantity}\n"

        return (
            f"{super().generate(products)}\n"
            "Produtos estocados por empresa:\n"
            f"{products_by_company_str}"
        )
