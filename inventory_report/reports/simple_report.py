from collections import Counter
from datetime import datetime


class SimpleReport:
    @classmethod
    def generate(cls, products: list[dict]) -> str:
        date_today = datetime.today().strftime("%Y-%m-%d")
        oldest_manufacturing_date = min(
            product["data_de_fabricacao"] for product in products
        )
        nearest_expiration_date = min(
            product["data_de_validade"]
            for product in products
            if product["data_de_validade"] > date_today
        )
        company_count = Counter(
            product["nome_da_empresa"] for product in products
        )
        company_with_more_products = company_count.most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_manufacturing_date}\n"
            f"Data de validade mais próxima: {nearest_expiration_date}\n"
            f"Empresa com mais produtos: {company_with_more_products}"
        )
