import csv
import os

ARQUIVO = "livros.csv"


def carregar_livros():
    livros = []

    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for livro in leitor:
                livro["ano"] = int(livro["ano"])
                livros.append(livro)

    return livros


def salvar_livros(livros):
    campos = ["titulo", "autor", "ano", "isbn", "status"]

    with open(ARQUIVO, "w", newline="", encoding="utf-8") as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(livros)


def cadastrar_livro(livros):
    print("\n--- CADASTRAR LIVRO ---")

    titulo = input("Titulo: ").strip()
    autor = input("Autor: ").strip()
    ano = input("Ano de publicacao: ").strip()
    isbn = input("Codigo/ISBN: ").strip()

    if titulo == "" or autor == "" or ano == "" or isbn == "":
        print("Preencha todos os campos.")
        return livros

    if not ano.isdigit():
        print("Digite um ano valido.")
        return livros

    for livro in livros:
        if livro["isbn"] == isbn:
            print("Esse ISBN ja esta cadastrado.")
            return livros

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": int(ano),
        "isbn": isbn,
        "status": "disponivel"
    }

    livros.append(novo_livro)
    salvar_livros(livros)

    print("Livro cadastrado com sucesso!")

    return livros


def encontrar_livro(livros, isbn):
    for livro in livros:
        if livro["isbn"] == isbn:
            return livro

    return None


def emprestar_livro(livros):
    print("\n--- EMPRESTIMO ---")

    isbn = input("Codigo/ISBN: ").strip()
    livro = encontrar_livro(livros, isbn)

    if livro is None:
        print("Livro nao encontrado.")

    elif livro["status"] == "emprestado":
        print("Esse livro ja esta emprestado.")

    else:
        livro["status"] = "emprestado"
        salvar_livros(livros)
        print("Emprestimo realizado com sucesso!")

    return livros


def devolver_livro(livros):
    print("\n--- DEVOLUCAO ---")

    isbn = input("Codigo/ISBN: ").strip()
    livro = encontrar_livro(livros, isbn)

    if livro is None:
        print("Livro nao encontrado.")

    elif livro["status"] == "disponivel":
        print("Esse livro ja esta disponivel.")

    else:
        livro["status"] = "disponivel"
        salvar_livros(livros)
        print("Devolucao realizada com sucesso!")

    return livros


def listar_livros(livros):
    print("\n--- LIVROS CADASTRADOS ---")

    if not livros:
        print("Nenhum livro cadastrado.")
        return livros

    for livro in livros:
        print(
            "Titulo:", livro["titulo"],
            "| Autor:", livro["autor"],
            "| Ano:", livro["ano"],
            "| ISBN:", livro["isbn"],
            "| Status:", livro["status"]
        )

    return livros


def buscar_livro(livros):
    print("\n--- BUSCAR LIVRO ---")

    termo = input("Digite o titulo ou autor: ").strip().lower()
    encontrados = []

    for livro in livros:
        if termo in livro["titulo"].lower() or termo in livro["autor"].lower():
            encontrados.append(livro)

    if not encontrados:
        print("Nenhum livro encontrado.")
    else:
        for livro in encontrados:
            print(
                "Titulo:", livro["titulo"],
                "| Autor:", livro["autor"],
                "| Ano:", livro["ano"],
                "| Status:", livro["status"]
            )

    return encontrados


def ordenar_livros(livros):
    print("\n--- ORDENAR LIVROS ---")
    print("1 - Titulo")
    print("2 - Autor")
    print("3 - Ano")

    opcao = input("Escolha: ").strip()

    if opcao == "1":
        livros.sort(key=lambda livro: livro["titulo"].lower())
        print("Livros ordenados por titulo.")

    elif opcao == "2":
        livros.sort(key=lambda livro: livro["autor"].lower())
        print("Livros ordenados por autor.")

    elif opcao == "3":
        livros.sort(key=lambda livro: livro["ano"])
        print("Livros ordenados por ano.")

    else:
        print("Opcao invalida.")
        return livros

    salvar_livros(livros)

    return livros


def mostrar_menu():
    print("\n==============================")
    print("        BIBLIOTECA")
    print("==============================")
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar livros")
    print("7 - Sair")
    print("==============================")


def main():
    livros = carregar_livros()

    while True:
        mostrar_menu()

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            livros = cadastrar_livro(livros)

        elif opcao == "2":
            livros = emprestar_livro(livros)

        elif opcao == "3":
            livros = devolver_livro(livros)

        elif opcao == "4":
            listar_livros(livros)

        elif opcao == "5":
            buscar_livro(livros)

        elif opcao == "6":
            livros = ordenar_livros(livros)

        elif opcao == "7":
            salvar_livros(livros)
            print("Programa encerrado.")
            break

        else:
            print("Opcao invalida.")

main()