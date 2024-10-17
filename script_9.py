with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("Representação original da linha")

    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))