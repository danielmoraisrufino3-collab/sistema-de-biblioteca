import csv
import os

ARQUIVO_LIVROS = "livros.csv"


def carregar_livros():
    """Carrega os livros salvos no arquivo CSV."""
    livros = []

    if not os.path.exists(ARQUIVO_LIVROS):
        return livros

    with open(ARQUIVO_LIVROS, "r", newline="", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)

        for livro in leitor:
            livro["ano"] = int(livro["ano"])
            livros.append(livro)

    return livros


def salvar_livros(livros):
    """Salva a lista de livros no arquivo CSV."""
    with open(ARQUIVO_LIVROS, "w", newline="", encoding="utf-8") as arquivo:
        campos = ["titulo", "autor", "ano", "isbn", "status"]

        escritor = csv.DictWriter(
            arquivo,
            fieldnames=campos
        )

        escritor.writeheader()
        escritor.writerows(livros)
