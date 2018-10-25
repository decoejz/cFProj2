import sys
from signalTeste import *
from funcoes import *
import sounddevice as sd
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

freq = 13000
amplitude = 5
time = 1 #seconds
fs = 44100
CONT = np.linspace(0, 88200, 88200)

#####AUDIO INICIAL######
# data, samplerate = sf.read('portadora.wav')
print('Comecou a gravar')
data = sd.rec(int(time * fs), samplerate=fs, channels=1)
sd.wait()
print('Acabou de gravar')

#####AUDIO NORMALIZADO######
print('Começando a normalizar')
normalizado = normaliza(data)

#####AUDIO FILTRADO######
print('Começando a filtrar')
filtrado = passaBaixa(normalizado,fs)

#####AUDIO MODULADO######
print('Começando a modular')
modulado = modula(filtrado,freq,time,fs)

#####GRAFICOS######
plt.plot(CONT,data)
plt.title('Sinal de áudio original')
plt.show()

plt.plot(CONT,normalizado)
plt.title('Sinal de áudio normalizado')
plt.show()

plt.plot(CONT,filtrado)
plt.title('Sinal de áudio filtrado')
plt.show()

plt.plot(CONT,modulado)
plt.title('Sinal de áudio modulado')
plt.show()

#####TOCANDO AUDIO MODULADO######
print('Resultado')
sd.play(modulado, fs)
sd.wait()