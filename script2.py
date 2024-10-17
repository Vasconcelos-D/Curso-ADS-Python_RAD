arquivo = open("dados.txt", "r", encoding='utf-8')

print("Iterando sobre o arquivo")

for linha in arquivo:
    print(repr(linha))
    
arquivo.close()

#usando for para pecorrer todas as linhas e imprimir na tela, usando para arquivos com muitas 
#linha de codigos. 