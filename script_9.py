
#Methodo count
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    text = arquivo.read()
    contador = text.count("Olá")

print("Total de Olás  = ", contador)
       
       