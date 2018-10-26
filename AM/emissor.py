import sys
from signalTeste import *
from funcoes import *
import sounddevice as sd
import matplotlib.pyplot as plt
import soundfile as sf
import sounddevice as sd

freq = 14000
amplitude = 5
time = 3 #seconds
fs = 44100
CONT = np.linspace(0, time*fs, time*fs)

#####AUDIO INICIAL######
# data, samplerate = sf.read('som.wav')
print('Comecou a gravar')
data = sd.rec(int(time * fs), samplerate=fs, channels=1)
sd.wait()
print('Acabou de gravar')
# sf.write('som.wav', data, fs)

#####AUDIO NORMALIZADO######
print('Começando a normalizar')
normalizado_Pre = normaliza(data)

normalizado = normalizado_Pre[:,0]

#####AUDIO FILTRADO######
print('Começando a filtrar')
filtrado = passaBaixa(normalizado,fs)

#####AUDIO MODULADO######

print('Começando a modular')
modulado = modula(filtrado,freq,time,fs)

#####GRAFICOS######
# sig = signalMeu()
print('Plotando os graficos')
plt.plot(CONT,data)
plt.title('Sinal de áudio original')
plt.show()
data=data[:,0]
plotandoFreq(data,fs)

print('Normalizado')
plt.plot(CONT,normalizado)
plt.title('Sinal de áudio normalizado')
plt.show()

plotandoFreq(normalizado,fs)
# sig.plotFFT(normalizado,fs)

print('Filtrado')
plt.plot(CONT,filtrado)
plt.title('Sinal de áudio filtrado')
plt.show()

plotandoFreq(filtrado,fs)

print('Modulado')
plt.plot(CONT,modulado)
plt.title('Sinal de áudio modulado')
plt.show()

plotandoFreq(modulado,fs)

# #####TOCANDO AUDIO MODULADO######
print('Resultado')
sd.play(modulado, fs)
sd.wait()