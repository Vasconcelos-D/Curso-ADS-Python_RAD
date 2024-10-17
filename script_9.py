# Frase 1: Define uma frase com várias palavras separadas por espaços
frase1 = "Eu amo comer amoras no café da manhã"

# Converte a frase em uma lista de palavras, separando pelos espaços (padrão do split)
lista_termos1 = frase1.split()

# Imprime a lista resultante com as palavras da frase
print(lista_termos1)


# Frase 2: Define uma sequência de palavras com múltiplos espaços entre elas
frase2 = "Amora  Abacaxi  Abacate  Banana"

# Converte a frase em uma lista de palavras, ignorando os espaços extras
lista_termos2 = frase2.split()

# Imprime a lista resultante com as frutas separadas
print(lista_termos2)


# Frase 3: Define uma frase com elementos separados por vírgulas
frase3 = "Carro,Moto,Avião"

# Converte a frase em uma lista, utilizando a vírgula como delimitador
lista_termos3 = frase3.split(",")

# Imprime a lista resultante com os elementos separados por vírgulas
print(lista_termos3)
