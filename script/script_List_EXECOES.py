import os

try:
    entradas = os.scandir("meu_diretorio")

    for obj in entradas:
        print("Nome:", obj.name)
        print("Caminho:", obj.path)
        print("É diretório:", obj.is_dir)
        print("É arquivo:", obj.is_file)
        if obj.is_file():
            print("Tamanho:", obj.stat().st_size, "8")
        print("=====================================")
except FileNotFoundError:
    print("O caminho não existe.")
except NotADirectoryError:
    print("O caminho não é de um diretório")