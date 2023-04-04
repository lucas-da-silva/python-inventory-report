from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, products):
        date_today = datetime.today().strftime("%Y-%m-%d")
        oldest_manufacturing_date = min(
            [company["data_de_fabricacao"] for company in products]
        )
        nearest_expiration_date = min([
            company["data_de_validade"]
            for company in products
            if company["data_de_validade"] > date_today
        ])
        company_count = dict()

        for company in products:
            if company["nome_da_empresa"] in company_count:
                company_count[company["nome_da_empresa"]] += 1
            else:
                company_count[company["nome_da_empresa"]] = 1
        company_with_more_products = max(company_count, key=company_count.get)

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
