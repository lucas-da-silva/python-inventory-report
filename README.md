# Python Inventory Reports
Aplicação que realiza a leitura de arquivos com dados de estoque e gera, como saída, um relatório acerca destes dados. 

Os dados de estoques são obtidos via arquivos que podem ser do tipo `JSON`, `CSV` ou `XML`. Além disso, o relatório final possuirá duas versões: simples e completa.


Foi utilizando no desenvolvimento os conceitos de Orientação a Objetos em Python, testes e padrões de projetos.

## Funcionalidades
- Leitura e escrita de arquivos (XML, CSV, JSON)
- Formatação dos dados para gerar relatórios

![Relatório](images/img1.png)

## Tecnologias

- [Python](https://www.python.org/) - Linguagem de programação focada em desenvolvimento rápido e integração de sistemas eficazmente
- [Pytest](https://docs.pytest.org/en/7.2.x/) - Framework que facilita a escrita de testes pequenos e legíveis

## Estrutura do projeto

```
$PROJECT_ROOT
|   # Código Python
├── inventory_report
│   |   # Arquivos com dados de estoque
|   ├── data
│   │   ├──  inventory.csv
│   │   ├──  inventory.json
│   │   └──  inventory.xml
│   |   # Classes responsáveis por ler arquivos
|   ├── importer
│   │   ├──  csv_importer.py
│   │   ├──  importer.py
│   │   ├──  json_importer.py
│   │   └──  xml_importer.py
│   |   # Classes que leem os arquivos e retornam relatórios
|   ├── inventory
│   │   ├──  inventory_iterator.py
│   │   ├──  inventory_refactor.py
│   │   └──  inventory.py
│   │   └──  product.py
|   |   # Classes que geram relatórios
│   ├── reports
│   │   ├──  colored_report.py
│   │   ├──  complete_report.py
│   │   └──  simple_report.py
│   └──  main.py
|   # Testes 
└── tests
```

## Como utilizar

Criando e ativando o ambiente virtual:

```bash
python3 -m venv .venv && source .venv/bin/activate
```

Instalando as dependências e o projeto no ambiente virtual

```bash
python3 -m pip install -r dev-requirements.txt && pip install .
```

Para gerar o relatório de arquivo, use o seguinte comando:

```bash
python3 inventory_report/main.py local_do_arquivo completo 
```

Exemplo:

```bash
python3 inventory_report/main.py inventory_report/data/inventory.csv completo
```