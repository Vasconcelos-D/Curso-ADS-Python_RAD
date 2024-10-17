arquivo = open("dados.txt", "r", encoding='utf-8')
conteudo = arquivo.read()
print ("Todo o conteúdo do arquivo")
print(repr(conteudo), '\n')

conteudo_releitura = arquivo.read()
print("Releitura de todo o conteúdo do arquivo")
print(repr(conteudo_releitura),'\n')

arquivo.close()

arquivo_reaberto = open("dados.txt", "r", encoding='utf-8')
conteudo_reaberto = arquivo_reaberto.read()
print("Todo o conteúdo do arquivo novamente")
print(repr(conteudo_reaberto),'\n')

arquivo_reaberto.seek(8)
conteudo_seek = arquivo_reaberto.read()
print("Todo conteúdo do arquivo após o SEEK")
print(repr(conteudo_seek))

arquivo_reaberto.close()
# todos em moto de leitura...