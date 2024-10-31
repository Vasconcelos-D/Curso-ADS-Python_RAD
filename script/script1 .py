linhas = ["Conteúdo da primeira linha.","\n Conteúdo da segunda linha."]

arquivo_escrita = open("dados.txt", "w", encoding="utf-8")
arquivo_escrita.writelines(linhas)
arquivo_escrita.close()