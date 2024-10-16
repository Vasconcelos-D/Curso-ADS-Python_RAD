import os
arquivo1 = open ("teste.txt", 'w', encoding='utf-8')
arquivo2 = open ("C:\\Users\\IFPB.IP\\Documents\\teste2.txt")

arquivo1.write("Olá mundo!!")

print ("Arquivo aberto com sucesso!")


print(os.path.relpath(arquivo1.name))
print(os.path.abspath(arquivo2.name))

print(arquivo1)
print(arquivo2)

arquivo1.close()
