#Testamdo frameworks de GUI
#Tkinter
#import tkinter
#tkinter._test()
#Sucess

from flexx import flx
class Exemplo(flx.Widget):
    def init(self):
        flx.Button(text='Olá')
        flx.Button(text='Mundo')

if __name__ == '__main__':
    a = flx.App(Exemplo, title = 'Flexx demostração')
    m = a.launch()
    flx.run()