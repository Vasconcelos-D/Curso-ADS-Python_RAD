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

#Widget Button

# import tkinter as tk
# def mostrar_nomes():
#    print("Nome: %s\nSobrenome: %s" % (e1.get(), e2.get()))
# janela = tk.Tk()
# janela.title("Aplicação GUI com o Widget Entry")
# tk.Label(janela,text="Nome").grid(row=0)

#Widget Entry

# tk.Label(janela,text="Sobrenome").grid(row=1)
# e1 = tk.Entry(janela)
# e2 = tk.Entry(janela)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# tk.Button(janela, text='Sair',command=janela.quit).grid(row=3,column=0,sticky=tk.W,pady=4)
# tk.Button(janela, text='Exibir Dados', command=mostrar_nomes).grid(row=3,column=1,sticky=tk.W,pady=4)
# tk.mainloop()


#Widget Radiobutton

# import tkinter as tk
# janela = tk.Tk()
# v = tk.IntVar()
# tk.Label(janela,text="""Escolha uma linguagem de programação:""",justify = tk.LEFT, padx = 20).pack()
# tk.Radiobutton(janela,text="python",padx = 25,variable=v,value=1).pack(anchor=tk.W)
# tk.Radiobutton(janela,text="C++",padx = 25,variable=v,value=2).pack(anchor=tk.W)
# janela.mainloop()

#Widget Checkbox

# import tkinter as tk
# from tkinter import ttk
# janela = tk.Tk()
# def escolha_carreira():
#    print("Gerencial: %d,\nTécnica : %d" % (var1.get(), var2.get()))
# ttk.Label(janela, text="Escolha sua vocação:").grid(row=0, sticky=tk.W)
# var1 = tk.IntVar()
# ttk.Checkbutton(janela, text="Gerencial", variable=var1).grid(row=1, sticky=tk.W)
# var2 = tk.IntVar()
# ttk.Checkbutton(janela, text="Técnica", variable=var2).grid(row=2, sticky=tk.W)
# ttk.Button(janela, text='Sair', command=janela.quit).grid(row=3, sticky=tk.W, pady=4)
# ttk.Button(janela, text='Mostrar', command=escolha_carreira).grid(row=4, sticky=tk.W, pady=4)
# janela.mainloop()

# Widget Text

# import tkinter as tk
# janela = tk.Tk()
# T = tk.Text(janela, height=2, width=30)
# T.pack()
# T.insert(tk.END, "Este é um texto\ncom duas linhas\n")
# tk.mainloop()


#WIDGET MESAGEM
# import tkinter as tk
# janela = tk.Tk()
# mensagem_para_usuario = "Esta é uma mensagem.\n(Pode ser bastante útil para o usuário)"
# msg = tk.Message(janela, text = mensagem_para_usuario)
# msg.config(bg='lightgreen', font=('times', 24, 'italic'))
# msg.pack()
# janela.mainloop()

# Widget Slider
# import tkinter as tk
# from tkinter import ttk
# def mostrar_valores():
#    print (w1.get(), w2.get())
# janela = tk.Tk()
# w1 = ttk.Scale(janela, from_=0, to=50)
# w1.pack()
# w2 = ttk.Scale(janela, from_=0, to=100, orient=tk.HORIZONTAL)
# w2.pack()
# ttk.Button(janela, text='Mostrar a Escala', command=mostrar_valores).pack()
# janela.mainloop()

# #Widgete DIALOG
# import tkinter as tk
# from tkinter import messagebox as mb
# def resposta():
#    mb.showerror("Resposta", "Desculpe, nenhuma resposta disponível!")
# def verificacao():
#    if mb.askyesno('Verificar', 'Realmente quer sair?'):
#       mb.showwarning('Yes', 'Ainda não foi implementado')
#    else:
#       mb.showinfo('No', 'A opção de Sair foi cancelada')
# tk.Button(text='Sair', command=verificacao).pack(fill=tk.X)
# tk.Button(text='Resposta', command=resposta).pack(fill=tk.X)
# tk.mainloop()

import tkinter as tk
from tkinter import ttk
# Criação de uma janela tkinter
janela = tk.Tk()
janela.title('Combobox')
janela.geometry('500x250')
# Componente Label
ttk.Label(janela, text = "Combobox Widget",background = 'green', foreground ="white",font = ("Times New Roman", 15)).grid(row = 0, column = 1)
# Componente Label
ttk.Label(janela, text = "Selecione um mês :",font = ("Times New Roman", 10)).grid(column = 0,row = 5, padx = 10, pady = 25)
# Componente Combobox
n = tk.StringVar()
escolha = ttk.Combobox(janela, width = 27, textvariable = n)
# Adição de itens no Combobox
escolha['values'] = (' Janeiro',' Fevereiro',' Março',' Abril',' Maio',' Junho',' Julho',' Agosto',' Setembro',' Outubro',' Novembro',' Dezembro')
escolha.grid(column = 1, row = 5)
escolha.current()
janela.mainloop()