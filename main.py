def carregar_livros():
    """Carrega os livros do arquivo CSV."""
    livros = []

    if not os.path.exists(ARQUIVO_LIVROS):
        return livros

    try:
        with open(ARQUIVO_LIVROS, "r", newline="", encoding="utf-8") as arquivo:
            leitor = csv.DictReader(arquivo)

            for livro in leitor:
                livro["ano"] = int(livro["ano"])
                livros.append(livro)

    except (ValueError, KeyError):
        print("Erro ao ler o arquivo de livros.")
        return []

    return livros
def cadastrar_livro(livros):
    """Cadastra um novo livro."""
    print("\n===== CADASTRO DE LIVRO =====")

    titulo = input("Digite o título: ").strip()
    autor = input("Digite o autor: ").strip()
    isbn = input("Digite o código/ISBN: ").strip()

    if titulo == "" or autor == "" or isbn == "":
        print("Todos os campos são obrigatórios.")
        return livros

    for livro in livros:
        if livro["isbn"] == isbn:
            print("Já existe um livro cadastrado com esse ISBN.")
            return livros

    while True:
        try:
            ano = int(input("Digite o ano de publicação: "))

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
def buscar_livro(livros):
    """Busca livros pelo título ou autor."""
    print("\n===== BUSCAR LIVRO =====")

    termo = input("Digite o título ou autor: ").strip().lower()

    if termo == "":
        print("Digite algum termo para realizar a busca.")
        return []

    resultados = []

    for livro in livros:
        titulo = livro["titulo"].lower()
        autor = livro["autor"].lower()

        if termo in titulo or termo in autor:
            resultados.append(livro)

    if len(resultados) == 0:
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