#arquivo = open("dados.txt", "r", encoding='utf-8')

#print("Iterando sobre o arquivo")

#for linha in arquivo:
 #   print(repr(linha))
    
#arquivo.close()

#usando for para pecorrer todas as linhas e imprimir na tela, usando para arquivos com muitas 
#linha de codigos. 

#Vamos usar agora o Wrint(Escrever no Python)

# Abre (ou cria) um arquivo chamado 'dados.txt' no modo de escrita ('w')
# O modo 'w' sobrescreve o conteúdo se o arquivo já existir
# 'encoding="utf-8"' define a codificação de caracteres como UTF-8
arquivo_escrita = open("dados.txt", "w", encoding='utf-8')
# Aqui você pode adicionar comandos para escrever no arquivo

# Escreve "Conteudo da primeira linha." no arquivo, mas ainda sem quebra de linha
arquivo_escrita.write("Conteudo da primeira linha.\n")  # O '\n' adiciona a quebra de linha

# Escreve "Conteudo da segunda linha." no arquivo, com uma nova quebra de linha
arquivo_escrita.write("Conteudo da segunda linha.\n")  # O '\n' garante que a linha termine corretamente





arquivo_escrita.close()

