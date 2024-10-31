import sqlite3 as conector

#Abertura de Conceção
conexao = conector.connect("URL SQLite")

#Criando um cursor
cursor = conexao.cursor()

#Executando os comandos: SELECT,CREAT
cursor.execute("SELECT")
cursor.fetchall()

#Efetivação do comando
conexao.commit()

#Fechando as conexões
cursor.close()
conexao.cursor()

#Boa pratica, utilizar sempre o metodo close()


