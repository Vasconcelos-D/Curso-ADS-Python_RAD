#Testamdo frameworks de GUI
#Tkinter
#import tkinter
#tkinter._test()
#Sucess

#Flexx
#from flexx import flx
#class Exemplo(flx.Widget):
#    def init(self):
#        flx.Button(text='Olá')
#        flx.Button(text='Mundo')

#if __name__ == '__main__':
#    a = flx.App(Exemplo, title = 'Flexx demostração')
#    m = a.launch()
#    flx.run()
#Sucess

# from cefpython3 import cefpython as cef
# import platform
# import sys

# def main():
#     verificar_versoes()
#     sys.excepthook = cef.ExceptHook  # Para fechar todos os processos CEF em caso de erro
#     cef.Initialize()
#     cef.CreateBrowserSync(url="https://www.google.com/", window_title="Olá, mundo! Este é o primeiro exemplo do CEF Python")
#     cef.MessageLoop()
#     cef.Shutdown()

# def verificar_versoes():
#     ver = cef.GetVersion()
#     print("[hello_world.py] CEF Python {ver}".format(ver=ver["version"]))
#     print("[hello_world.py] Chromium {ver}".format(ver=ver["chrome_version"]))
#     print("[hello_world.py] CEF {ver}".format(ver=ver["cef_version"]))
#     print("[hello_world.py] Python {ver} {arch}".format(ver=platform.python_version(), arch=platform.architecture()[0]))
#     assert cef.__version__ >= "57.0", "É necessário CEF Python v57.0+ para rodar este script"

# if __name__ == '__main__':
#     main()

# from kivy.app import App
# from kivy.uix.button import Button

# class ExemploApp(App):
#     def build(self):
#         return Button(text='Olá, Mundo!')

import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton

class ExemploSimples(BaseWidget):

    def __init__(self):
        super(ExemploSimples,self).__init__('ExemploSimples')
        #Definition of the forms fields
        self._nome = ControlText('Nome', 'Default value')
        self._sobrename = ControlText('Sobrenome')
        self._nomeCompleto = ControlText('Nome completo')
        self._button = ControlButton('Pressione o Botão')


#Execute the application
if __name__ == "__main__":
    from pyforms import start_app
    start_app(ExemploSimples)