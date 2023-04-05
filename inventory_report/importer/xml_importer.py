from bs4 import BeautifulSoup
from inventory_report.importer.importer import Importer


def parse_record(record):
    return {
        "id": record.find("id").text,
        "nome_do_produto": record.find("nome_do_produto").text,
        "nome_da_empresa": record.find("nome_da_empresa").text,
        "data_de_fabricacao": record.find("data_de_fabricacao").text,
        "data_de_validade": record.find("data_de_validade").text,
        "numero_de_serie": record.find("numero_de_serie").text,
        "instrucoes_de_armazenamento": record.find(
            "instrucoes_de_armazenamento"
        ).text,
    }


class XmlImporter(Importer):
    @classmethod
    def import_data(cls, path):
        if not path.endswith(".xml"):
            raise ValueError("Arquivo inválido")
        with open(path) as file:
            soup = BeautifulSoup(file, "xml")
            records = soup.find_all("record")
            products = [parse_record(record) for record in records]
            return products
