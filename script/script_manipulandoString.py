# Readlines

arquivo = open("dados.txt", 'r', encoding='utf-8')
conteudo = arquivo.readlines()

print("Tipo de conteúdo:", type(conteudo))
print("Conteúdo retornado pelo read:")
print(repr(conteudo))

arquivo.close()
