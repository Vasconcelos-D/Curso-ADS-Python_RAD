import os

try:
    os.remove("dados.txt")
    print("Arquivo removido!")
except FileNotFoundError as erro:
    print("Arquivo inexistente")
    print("Descrição", erro)
except PermissionError as erro:
    print("Sem permissão para acessar o arquivo")
    print("Descrição", erro)
except IsADirectoryError as erro:
    print("Remove serve apenas para serviços")
    print("Descrição", erro)

print("Termino do programa")