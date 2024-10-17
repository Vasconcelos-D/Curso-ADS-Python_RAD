arquivo = open("dados.txt", "r", encoding='utf-8')
conteudo = arquivo.read()
print ("Todo o conteúdo do arquivo")
print(repr(conteudo), '\n')

conteudo_releitura = arquivo.read()
print("Releitura de todo o conteúdo do arquivo")
print(repr(conteudo_releitura),'\n')

arquivo.close()