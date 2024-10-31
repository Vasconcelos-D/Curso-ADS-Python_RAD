minha_lista = ['Arroz', 'Feijão', 'Macarrão']
text_1 = ", ".join(minha_lista)
with open('dados.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(text_1)

texto_2 = '\n'.join(minha_lista)
with open('dados2.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.write(texto_2)