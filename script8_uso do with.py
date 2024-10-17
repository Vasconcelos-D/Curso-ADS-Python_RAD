# Inicia a impressão de uma mensagem indicando que a iteração sobre o arquivo vai começar
print("Iterando sobre o arquivo")

# Abre o arquivo "dados.txt" em modo de leitura ('r') com codificação UTF-8
with open("dados.txt", "r", encoding='utf-8') as arquivo:
    # Itera sobre cada linha do arquivo
    for linha in arquivo:
        # Imprime a linha atual, sem adicionar uma nova linha extra
        print(linha, end='')  # O parâmetro end='' evita a quebra de linha adicional
    # Após ler todo o arquivo, imprime uma mensagem indicando que a leitura foi concluída
    print("\nFim do arquivo:", arquivo.name)  # Mostra o nome do arquivo lido
