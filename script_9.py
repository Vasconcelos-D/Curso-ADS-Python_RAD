with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("Representação original da linha")

    for linha in arquivo:
        print(repr(linha))