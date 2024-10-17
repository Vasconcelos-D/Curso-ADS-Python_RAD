# Frase 1: Define uma frase com várias palavras separadas por espaços
frase1 = "Eu amo comer amoras no café da manhã"

print("Contagem direta:", frase1.count('amo'))
contador = 0

lista_termos1 = frase1.split()
for termo in lista_termos1:
    if termo == 'amo':
        contador += 1
print("Contagem correta:", contador)