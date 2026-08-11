import csv
import os

ARQUIVO = "livros.csv"


def carregar():
    livros = []

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for livro in leitor:
                livro["ano"] = int(livro["ano"])
                livros.append(livro)

    return livros


def salvar(livros):
    campos = ["titulo", "autor", "ano", "isbn", "status"]

    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(livros)


def cadastrar(livros):
    print("\n--- CADASTRAR LIVRO ---")

    titulo = input("Título: ")
    autor = input("Autor: ")
    ano = input("Ano: ")
    isbn = input("ISBN: ")

    if titulo == "" or autor == "" or ano == "" or isbn == "":
        print("Preencha todos os campos.")
        return livros

    for livro in livros:
        if livro["isbn"] == isbn:
            print("ISBN já cadastrado.")
            return livros

    if not ano.isdigit():
        print("Ano inválido.")
        return livros

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": int(ano),
        "isbn": isbn,
        "status": "disponível"
    }

    livros.append(novo_livro)
    salvar(livros)

    print("Livro cadastrado!")
    return livros


def encontrar(livros, isbn):
    for livro in livros:
        if livro["isbn"] == isbn:
            return livro
    return None


def emprestar(livros):
    isbn = input("ISBN do livro: ")
    livro = encontrar(livros, isbn)

    if livro is None:
        print("Livro não encontrado.")
    elif livro["status"] == "emprestado":
        print("Livro já está emprestado.")
    else:
        livro["status"] = "emprestado"
        salvar(livros)
        print("Empréstimo realizado!")

    return livros


def devolver(livros):
    isbn = input("ISBN do livro: ")
    livro = encontrar(livros, isbn)

    if livro is None:
        print("Livro não encontrado.")
    elif livro["status"] == "disponível":
        print("Livro já está disponível.")
    else:
        livro["status"] = "disponível"
        salvar(livros)
        print("Devolução realizada!")

    return livros


def listar(livros):
    print("\n--- LIVROS ---")

    if not livros:
        print("Nenhum livro cadastrado.")
        return livros

    for livro in livros:
        print(
            f"{livro['titulo']} | "
            f"{livro['autor']} | "
            f"{livro['ano']} | "
            f"{livro['isbn']} | "
            f"{livro['status']}"
        )

    return livros


def buscar(livros):
    termo = input("Digite o título ou autor: ").lower()
    encontrados = []

    for livro in livros:
        if termo in livro["titulo"].lower() or termo in livro["autor"].lower():
            encontrados.append(livro)

    if encontrados:
        for livro in encontrados:
            print(
                f"{livro['titulo']} | "
                f"{livro['autor']} | "
                f"{livro['ano']} | "
                f"{livro['status']}"
            )
    else:
        print("Nenhum livro encontrado.")

    return encontrados


def ordenar(livros):
    print("1 - Título")
    print("2 - Autor")
    print("3 - Ano")

    opcao = input("Ordenar por: ")

    if opcao == "1":
        livros.sort(key=lambda livro: livro["titulo"].lower())
    elif opcao == "2":
        livros.sort(key=lambda livro: livro["autor"].lower())
    elif opcao == "3":
        livros.sort(key=lambda livro: livro["ano"])
    else:
        print("Opção inválida.")
        return livros

    salvar(livros)
    print("Livros ordenados!")

    return livros


livros = carregar()

while True:
    print("\n===== BIBLIOTECA =====")
    print("1 - Cadastrar")
    print("2 - Emprestar")
    print("3 - Devolver")
    print("4 - Listar")
    print("5 - Buscar")
    print("6 - Ordenar")
    print("7 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        livros = cadastrar(livros)
    elif opcao == "2":
        livros = emprestar(livros)
    elif opcao == "3":
        livros = devolver(livros)
    elif opcao == "4":
        listar(livros)
    elif opcao == "5":
        buscar(livros)
    elif opcao == "6":
        livros = ordenar(livros)
    elif opcao == "7":
        salvar(livros)
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")