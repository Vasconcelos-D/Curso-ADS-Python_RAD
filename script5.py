arquivo = open("dados.txt", "r", encoding= 'utf-8')
conteudo = arquivo.readlines()

print("Tipo do conteúdo" , type(conteudo))

print("Conteúdo retornado pelo readlines:")
print(repr(conteudo))

arquivo.close()