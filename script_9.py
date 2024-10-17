
#Methodo Scriit
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    print("Representação original da linha")
    contador = 0
    for linha in arquivo:
        if linha:
            contador += 1
            print("Total  = ", contador)
       
       