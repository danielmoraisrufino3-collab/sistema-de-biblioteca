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

    livros.append(novo_livro)
    salvar_livros(livros)

    print("Livro cadastrado com sucesso!")

    return livros


def encontrar_livro(livros, isbn):
    """Encontra um livro pelo código/ISBN."""
    for livro in livros:
        if livro["isbn"] == isbn:
            return livro

    return None


def emprestar_livro(livros):
    """Registra o empréstimo de um livro."""
    print("\n--- EMPRESTAR LIVRO ---")

    isbn = input("Digite o código/ISBN: ").strip()

    livro = encontrar_livro(livros, isbn)

    if livro is None:
        print("Livro não encontrado.")
        return livros

    if livro["status"] == "emprestado":
        print("Este livro já está emprestado.")
        return livros

    livro["status"] = "emprestado"

    salvar_livros(livros)

    print("Empréstimo registrado com sucesso!")

    return livros


def devolver_livro(livros):
    """Registra a devolução de um livro."""
    print("\n--- DEVOLVER LIVRO ---")

    isbn = input("Digite o código/ISBN: ").strip()

    livro = encontrar_livro(livros, isbn)

    if livro is None:
        print("Livro não encontrado.")
        return livros

    if livro["status"] == "disponível":
        print("Este livro já está disponível.")
        return livros

    livro["status"] = "disponível"

    salvar_livros(livros)

    print("Devolução registrada com sucesso!")

    return livros


def listar_livros(livros):
    """Lista todos os livros cadastrados."""
    print("\n--- LISTA DE LIVROS ---")

    if not livros:
        print("Nenhum livro cadastrado.")
        return livros

    for numero, livro in enumerate(livros, start=1):
        print(
            f"{numero}. "
            f"Título: {livro['titulo']} | "
            f"Autor: {livro['autor']} | "
            f"Ano: {livro['ano']} | "
            f"ISBN: {livro['isbn']} | "
            f"Status: {livro['status']}"
        )

    return livros


def buscar_livro(livros):
    """Busca livros pelo título ou autor."""
    print("\n--- BUSCAR LIVRO ---")

    termo = input("Digite o título ou autor: ").strip().lower()

    resultados = []

    for livro in livros:
        if (
            termo in livro["titulo"].lower()
            or termo in livro["autor"].lower()
        ):
            resultados.append(livro)

    if not resultados:
        print("Nenhum livro encontrado.")
    else:
        print("\nLivros encontrados:")

        for livro in resultados:
            print(
                f"Título: {livro['titulo']} | "
                f"Autor: {livro['autor']} | "
                f"Ano: {livro['ano']} | "
                f"ISBN: {livro['isbn']} | "
                f"Status: {livro['status']}"
            )

    return resultados


def ordenar_livros(livros):
    """Ordena os livros por título, autor ou ano."""
    print("\n--- ORDENAR LIVROS ---")
    print("1 - Título")
    print("2 - Autor")
    print("3 - Ano")

    opcao = input("Escolha o critério: ").strip()

    if opcao == "1":
        livros.sort(
            key=lambda livro: livro["titulo"].lower()
        )
        print("Livros ordenados por título.")

    elif opcao == "2":
        livros.sort(
            key=lambda livro: livro["autor"].lower()
        )
        print("Livros ordenados por autor.")

    elif opcao == "3":
        livros.sort(
            key=lambda livro: livro["ano"]
        )
        print("Livros ordenados por ano.")

    else:
        print("Opção inválida.")

    salvar_livros(livros)

    return livros


def exibir_menu():
    """Exibe o menu principal do sistema."""
    print("\n" + "=" * 50)
    print("       SISTEMA DE GERENCIAMENTO DE BIBLIOTECA")
    print("=" * 50)
    print("1 - Cadastrar livro")
    print("2 - Emprestar livro")
    print("3 - Devolver livro")
    print("4 - Listar livros")
    print("5 - Buscar livro")
    print("6 - Ordenar livros")
    print("7 - Sair")
    print("=" * 50)


def main():
    """Função principal do sistema."""
    livros = carregar_livros()

    while True:
        exibir_menu()

        opcao = input("Escolha uma opção: ").strip()

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
            print("Sistema encerrado. Até logo!")
            break

        else:
            print("Opção inválida. Escolha uma opção de 1 a 7.")


if __name__ == "__main__":
    main()