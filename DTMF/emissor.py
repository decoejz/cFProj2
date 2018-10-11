<<<<<<< HEAD
import sys
if sys.platform == 'darwin':
    import matplotlib
    matplotlib.use('TkAgg')

import tkinter as tk
from signalTeste import *
import sounddevice as sd

class Teclado:
    def __init__(self):
        #Criando a janela gráfica e suas diretrizes
        self.window = tk.Tk()
        self.window.title('Teclado')
        self.window.geometry("300x350+600+55")
        
        #Criando as linhas e colunas do jogo
        self.window.rowconfigure(0, minsize=50, weight=1)
        self.window.rowconfigure(1, minsize=50, weight=1)
        self.window.rowconfigure(2, minsize=50, weight=1)
        self.window.rowconfigure(3, minsize=50, weight=1)
        
        self.window.columnconfigure(0, minsize=50, weight=1)
        self.window.columnconfigure(1, minsize=50, weight=1)
        self.window.columnconfigure(2, minsize=50, weight=1)
        
        #Criando os nove botões do jogo
        self.botao1 = tk.Button(self.window)
        self.botao1.grid(row=0,column=0, sticky='nsew')
        self.botao1['text'] = '1'
        self.botao1['font'] = 'bold'
        
        self.botao2 = tk.Button(self.window)
        self.botao2.grid(row=0,column=1, sticky='nsew')
        self.botao2['text'] = '2'

        self.botao3 = tk.Button(self.window)
        self.botao3.grid(row=0,column=2, sticky='nsew')
        self.botao3['text'] = '3'

        self.botao4 = tk.Button(self.window)
        self.botao4.grid(row=1,column=0, sticky='nsew')
        self.botao4['text'] = '4'

        self.botao5 = tk.Button(self.window)
        self.botao5.grid(row=1,column=1, sticky='nsew')
        self.botao5['text'] = '5'

        self.botao6 = tk.Button(self.window)
        self.botao6.grid(row=1,column=2, sticky='nsew')
        self.botao6['text'] = '6'

        self.botao7 = tk.Button(self.window)
        self.botao7.grid(row=2,column=0, sticky='nsew')
        self.botao7['text'] = '7'

        self.botao8 = tk.Button(self.window)
        self.botao8.grid(row=2,column=1, sticky='nsew')
        self.botao8['text'] = '8'

        self.botao9 = tk.Button(self.window)
        self.botao9.grid(row=2,column=2, sticky='nsew')
        self.botao9['text'] = '9'

        self.botao0 = tk.Button(self.window)
        self.botao0.grid(row=3,column=1, sticky='nsew')
        self.botao0['text'] = '0'

        self.botao0.bind('<1>',self.clicar_botao_0)
        self.botao1.bind('<1>',self.clicar_botao_1)
        self.botao2.bind('<1>',self.clicar_botao_2)
        self.botao3.bind('<1>',self.clicar_botao_3)
        self.botao4.bind('<1>',self.clicar_botao_4)
        self.botao5.bind('<1>',self.clicar_botao_5)
        self.botao6.bind('<1>',self.clicar_botao_6)
        self.botao7.bind('<1>',self.clicar_botao_7)
        self.botao8.bind('<1>',self.clicar_botao_8)
        self.botao9.bind('<1>',self.clicar_botao_9)

        self.window.bind("<KeyRelease-0>", self.clicar_botao_0)
        self.window.bind("<KeyRelease-1>", self.clicar_botao_1)
        self.window.bind("<KeyRelease-2>", self.clicar_botao_2)
        self.window.bind("<KeyRelease-3>", self.clicar_botao_3)
        self.window.bind("<KeyRelease-4>", self.clicar_botao_4)
        self.window.bind("<KeyRelease-5>", self.clicar_botao_5)
        self.window.bind("<KeyRelease-6>", self.clicar_botao_6)
        self.window.bind("<KeyRelease-7>", self.clicar_botao_7)
        self.window.bind("<KeyRelease-8>", self.clicar_botao_8)
        self.window.bind("<KeyRelease-9>", self.clicar_botao_9)

        self.sig = signalMeu()
        self.freq1 = 1209
        self.freq2 = 1336
        self.freq3 = 1477
        self.freq4 = 697
        self.freq5 = 770
        self.freq6 = 852
        self.freq7 = 941
        self.amplitude = 0.5
        self.time = 1
        self.fs = 44100

    def iniciar(self):
        self.window.mainloop()
    
    def clicar_botao_1(self, event):
        x, sinal1 = self.sig.generateSin(self.freq1, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq4, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        self.plot_grafico(sinal)

    def clicar_botao_2(self, event):
        x, sinal1 = self.sig.generateSin(self.freq2, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq4, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        self.plot_grafico(sinal)

    def clicar_botao_3(self, event):
        x, sinal1 = self.sig.generateSin(self.freq3, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq4, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        self.plot_grafico(sinal)
        
    def clicar_botao_4(self, event):
        x, sinal1 = self.sig.generateSin(self.freq1, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq5, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        self.plot_grafico(sinal)

    def clicar_botao_5(self, event):
        x, sinal1 = self.sig.generateSin(self.freq2, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq5, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        self.plot_grafico(sinal)
        
    def clicar_botao_6(self, event):
        x, sinal1 = self.sig.generateSin(self.freq3, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq5, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        self.plot_grafico(sinal)

    def clicar_botao_7(self, event):
        x, sinal1 = self.sig.generateSin(self.freq1, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq6, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        self.plot_grafico(sinal)
        
    def clicar_botao_8(self, event):
        x, sinal1 = self.sig.generateSin(self.freq2, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq6, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        self.plot_grafico(sinal)

    def clicar_botao_9(self, event):
        x, sinal1 = self.sig.generateSin(self.freq3, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq6, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        self.plot_grafico(sinal)
        
    def clicar_botao_0(self, event):
        x, sinal1 = self.sig.generateSin(self.freq2, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq7, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        self.plot_grafico(sinal)
    
    def plot_grafico(self,sinal):
        self.sig.plotFFT(sinal,self.fs)
        
teclado = Teclado()
teclado.iniciar()
=======
import sys
if sys.platform == 'darwin':
    import matplotlib
    matplotlib.use('TkAgg')

import tkinter as tk
from signalTeste import *
import sounddevice as sd

class Teclado:
    def __init__(self):
        #Criando a janela gráfica e suas diretrizes
        self.window = tk.Tk()
        self.window.title('Teclado')
        self.window.geometry("300x350+600+55")
        
        #Criando as linhas e colunas do jogo
        self.window.rowconfigure(0, minsize=50, weight=1)
        self.window.rowconfigure(1, minsize=50, weight=1)
        self.window.rowconfigure(2, minsize=50, weight=1)
        self.window.rowconfigure(3, minsize=50, weight=1)
        
        self.window.columnconfigure(0, minsize=50, weight=1)
        self.window.columnconfigure(1, minsize=50, weight=1)
        self.window.columnconfigure(2, minsize=50, weight=1)
        
        #Criando os nove botões do jogo
        self.botao1 = tk.Button(self.window)
        self.botao1.grid(row=0,column=0, sticky='nsew')
        self.botao1['text'] = '1'
        
        self.botao2 = tk.Button(self.window)
        self.botao2.grid(row=0,column=1, sticky='nsew')
        self.botao2['text'] = '2'

        self.botao3 = tk.Button(self.window)
        self.botao3.grid(row=0,column=2, sticky='nsew')
        self.botao3['text'] = '3'

        self.botao4 = tk.Button(self.window)
        self.botao4.grid(row=1,column=0, sticky='nsew')
        self.botao4['text'] = '4'

        self.botao5 = tk.Button(self.window)
        self.botao5.grid(row=1,column=1, sticky='nsew')
        self.botao5['text'] = '5'

        self.botao6 = tk.Button(self.window)
        self.botao6.grid(row=1,column=2, sticky='nsew')
        self.botao6['text'] = '6'

        self.botao7 = tk.Button(self.window)
        self.botao7.grid(row=2,column=0, sticky='nsew')
        self.botao7['text'] = '7'

        self.botao8 = tk.Button(self.window)
        self.botao8.grid(row=2,column=1, sticky='nsew')
        self.botao8['text'] = '8'

        self.botao9 = tk.Button(self.window)
        self.botao9.grid(row=2,column=2, sticky='nsew')
        self.botao9['text'] = '9'

        self.botao0 = tk.Button(self.window)
        self.botao0.grid(row=3,column=1, sticky='nsew')
        self.botao0['text'] = '0'

        #Apertando o botão direito do mouse em cada botão do jogo.
        self.botao1.bind('<1>',self.clicar_botao_1)
        self.botao1.bind("1", self.clicar_botao_1)
        self.botao2.bind('<1>',self.clicar_botao_2)
        self.botao2.bind("2", self.clicar_botao_2)
        self.botao3.bind('<1>',self.clicar_botao_3)
        self.botao4.bind('<1>',self.clicar_botao_4)
        self.botao5.bind('<1>',self.clicar_botao_5)
        self.botao6.bind('<1>',self.clicar_botao_6)
        self.botao7.bind('<1>',self.clicar_botao_7)
        self.botao8.bind('<1>',self.clicar_botao_8)
        self.botao9.bind('<1>',self.clicar_botao_9)
        self.botao0.bind('<1>',self.clicar_botao_0)

        self.sig = signalMeu()
        self.freq1 = 1209
        self.freq2 = 1336
        self.freq3 = 1477
        self.freq4 = 697
        self.freq5 = 770
        self.freq6 = 852
        self.freq7 = 941
        self.amplitude = 0.5
        self.time = 1
        self.fs = 44100

    def iniciar(self):
        self.window.mainloop()
    
    def clicar_botao_1(self, event):
        x, sinal1 = self.sig.generateSin(self.freq1, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq4, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)

    def clicar_botao_2(self, event):
        x, sinal1 = self.sig.generateSin(self.freq2, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq4, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)

    def clicar_botao_3(self, event):
        x, sinal1 = self.sig.generateSin(self.freq3, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq4, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        
    def clicar_botao_4(self, event):
        x, sinal1 = self.sig.generateSin(self.freq1, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq5, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)

    def clicar_botao_5(self, event):
        x, sinal1 = self.sig.generateSin(self.freq2, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq5, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        
    def clicar_botao_6(self, event):
        x, sinal1 = self.sig.generateSin(self.freq3, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq5, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)

    def clicar_botao_7(self, event):
        x, sinal1 = self.sig.generateSin(self.freq1, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq6, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        
    def clicar_botao_8(self, event):
        x, sinal1 = self.sig.generateSin(self.freq2, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq6, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)

    def clicar_botao_9(self, event):
        x, sinal1 = self.sig.generateSin(self.freq3, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq6, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
        
    def clicar_botao_0(self, event):
        x, sinal1 = self.sig.generateSin(self.freq2, self.amplitude, self.time, self.fs)
        x, sinal2 = self.sig.generateSin(self.freq7, self.amplitude, self.time, self.fs)
        sinal = sinal1 + sinal2
        sd.play(sinal, self.fs)
                
        
teclado = Teclado()
teclado.iniciar()
>>>>>>> bebd1a3afa30341f05d56ce1a4fd6cf5efe4bbf4
