# import tkinter as tk  # Importa a biblioteca tkinter, que permite criar interfaces gráficas em Python.

# contador = 0  # Define uma variável global 'contador' iniciada em 0, que será usada para contar os segundos.

# # Função que configura o contador para atualizar o rótulo (label) a cada segundo
# def contador_label(lblRotulo):
#     # Função interna que incrementa e atualiza o contador
#     def funcao_contar():
#         global contador  # Indica que usaremos a variável global 'contador'
#         contador += 1  # Incrementa o valor de 'contador' em 1
#         lblRotulo.config(text=str(contador))  # Atualiza o texto do label com o valor atual do contador
#         lblRotulo.after(1000, funcao_contar)  # Agenda a próxima chamada de 'funcao_contar' para 1 segundo depois

#     funcao_contar()  # Inicia o processo de contagem chamando a função 'funcao_contar'

# # Configura a janela principal da interface gráfica
# janela = tk.Tk()  # Cria a janela principal da aplicação
# janela.title("Contagem dos Segundos")  # Define o título da janela

# # Cria um rótulo (label) para exibir o contador na tela
# lblRotulo = tk.Label(janela, fg="green")  # Cria um label com o texto em verde
# lblRotulo.pack()  # Adiciona o label à janela e o posiciona automaticamente

# # Inicia a função que atualiza o contador a cada segundo
# contador_label(lblRotulo)  # Chama a função que iniciará a contagem no label

# # Cria um botão que permite ao usuário interromper e fechar o programa
# btnAcao = tk.Button(janela, text='Clique aqui para Interromper a contagem', width=50, command=janela.destroy)
# # 'command=janela.destroy' define que, ao clicar no botão, a janela será fechada e a contagem interrompida
# btnAcao.pack()  # Adiciona o botão à janela e o posiciona automaticamente

# # Executa o loop principal da interface gráfica para manter a janela aberta
# janela.mainloop()  # Mantém a janela aberta e em execução até que seja fechada pelo usuário

import tkinter as tk
def mostrar_nomes():
   print("Nome: %s\nSobrenome: %s" % (e1.get(), e2.get()))
janela = tk.Tk()
janela.title("Aplicação GUI com o Widget Entry")
tk.Label(janela,text="Nome").grid(row=0)

tk.Label(janela,text="Sobrenome").grid(row=1)
e1 = tk.Entry(janela)
e2 = tk.Entry(janela)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
tk.Button(janela, text='Sair',command=janela.quit).grid(row=3,column=0,sticky=tk.W,pady=4)
tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=3,column=1,sticky=tk.W,pady=4)
tk.mainloop()
