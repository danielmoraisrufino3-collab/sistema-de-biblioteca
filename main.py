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
def cadastrar_livro(livros):
    """Cadastra um novo livro."""
    print("\n--- CADASTRAR LIVRO ---")

    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    isbn = input("Código/ISBN: ").strip()

    if not titulo or not autor or not isbn:
        print("Todos os campos são obrigatórios.")
        return livros

    for livro in livros:
        if livro["isbn"] == isbn:
            print("Já existe um livro com esse código/ISBN.")
            return livros

    while True:
        try:
            ano = int(input("Ano de publicação: "))

            if ano > 0:
                break

            print("Digite um ano válido.")

        except ValueError:
            print("Digite apenas números para o ano.")

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "disponível"
    }
