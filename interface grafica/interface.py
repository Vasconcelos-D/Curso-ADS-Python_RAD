#Primeiro contato com inteface Grafica 

import tkinter as tk #importanto a Biblioteca
from tkinter import ttk
janela = tk.Tk() #Criado instância da classe TK no objeto janela.
janela.title("Aplicação GUI com Widget Label") #Uso do methodo title para definir um titulo.
#janela.resizable(False, False) Deixar o tamanho fixo da janela...
ttk.Label(janela, text= "Componete Label").grid(column=0, row=0)
janela.mainloop() #Evento iniciar um loop

