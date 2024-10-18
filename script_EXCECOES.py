import os
'''
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
'''
try:
    
    os.mkdir("meu_diretorio") #para adicionar o diretorio usa-se MKDIR
   #os.rmdir("meu_diretorio") # para remover usa-se RMDIR
    print("Diretório criado!")
except PermissionError as erro:
    print("Sem permissão para criar diretório")
    print("Descrição", erro)
except FileExistsError as erro:
    print("Diretório já existe")
    print("Descrição", erro)

print("Término do programa")