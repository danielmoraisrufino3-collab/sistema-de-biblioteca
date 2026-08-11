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