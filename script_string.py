'''from datetime import datetime

nome = "Alucard"
idade = 25

mensagem = f"Olá, {nome}. Você tem {idade} anos."

print(mensagem)


nome1 = "Dracula"
idade2 = 800
mensagem1 = "Ola, {}. Você tem {} anos.".format(nome1,idade2)
print(mensagem1)


valor = 3.14159
print("PI com 2 casas decimais: {:.2f}".format(valor))

valor1 = 3.14159
print(f"PI com 2 casas decimais: {valor1:.2f}") 

nome_3 = "João"
minha_string1 = "Olá " + nome_3 + "."
minha_string2 = f"Olá, {nome_3}."
minha_string3 = f"Olá, {nome_3.upper()}."
minha_string4 = f"Quantos anos vc tem? {10+8}."
minha_string5 = f"O número 2 é maior que o número 1? {2 > 1}."
minha_string6 = f"O número 2 está contido na lista [4, 5, 6]? {2 in{4, 5, 6}}."

print(minha_string1)
print(minha_string2)
print(minha_string3)
print(minha_string4)
print(minha_string5)
print(minha_string6)

frutas = ['Jabuticaba', 'Laranja', 'Uva', 'Banana']
for fruta in frutas:
    minha_fruta = f"Nome: {fruta:12} - Número de letras: {len(fruta): 3}"
    print(minha_fruta)
print()

pi = 3.14159
meu_numero = f'O número PI é: {pi:.1f}'
meu_numero_descolado = f'O número PI deslocado é : {pi:6.1f}'
meu_numero_preciso = f'O número Pi mais preciso é: {pi:.4f}'

print(meu_numero)
print(meu_numero_descolado)
print(meu_numero_preciso)

print()

data = datetime.now()
minha_data = f'A data de hoje é: {data}'
minha_data_formatada = f'A data de hoje formatada é {data:%d/%m/%y}'

print(minha_data)
print(minha_data_formatada)
'''
def zenit_polar_replace(text):
    # Aplicar a codificação ZENIT POLAR utilizando o método replace
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for old, new in replacements:
        text = text.replace(old, new)
    return text
 
def main():
    # Entrada da frase e aplicação da codificação
    phrase = "The quick brown fox jumps over the lazy dog"
    phrase = phrase.title()  # Primeira letra de cada palavra em maiúscula
 
    # Dividir a frase em palavras
    words = phrase.split()
 
    # Processar cada palavra na lista usando ZENIT POLAR
    coded_words = [zenit_polar_replace(word) for word in words]
 
    # Juntar todas as palavras codificadas em uma frase
    coded_phrase = " ".join(coded_words)
    print("Original:", phrase)
    print("Coded:", coded_phrase)
 
if __name__ == "__main__":
    main()
# CODIFICANDO PALAVRAS EM PYTHON